import time

from app.database import SessionLocal
from app import models
from app.queue import (
    redis_client,
    QUEUE_NAME,
    MAX_ATTEMPTS,
    enqueue_job,
    move_to_dead_letter,
)
from app.tasks import run_task


def process_one(job_id):
    db = SessionLocal()
    try:
        job = db.get(models.Job, job_id)
        if job is None:
            print(f"Job {job_id} not found in database, skipping")
            return
        attempt = job.attempts + 1
        print(f"Picked up job {job.id} ({job.task_type}), attempt {attempt}")
        job.status = "running"
        job.attempts = attempt
        db.commit()
        try:
            result = run_task(job.task_type, job.payload)
            job.status = "success"
            job.result = str(result)
            db.commit()
            print(f"Job {job.id} succeeded with result: {result}")
        except Exception as error:
            if job.attempts < MAX_ATTEMPTS:
                job.status = "pending"
                job.result = f"attempt {job.attempts} failed: {error}"
                db.commit()
                enqueue_job(job.id)
                print(f"Job {job.id} failed on attempt {job.attempts}, will retry: {error}")
            else:
                job.status = "failed"
                job.result = f"failed after {job.attempts} attempts: {error}"
                db.commit()
                move_to_dead_letter(job.id)
                print(f"Job {job.id} permanently failed after {job.attempts} attempts: {error}")
    finally:
        db.close()


def main():
    print("Worker started. Waiting for jobs...")
    while True:
        job_id = redis_client.lpop(QUEUE_NAME)
        if job_id is None:
            time.sleep(1)
            continue
        process_one(int(job_id))


if __name__ == "__main__":
    main()
