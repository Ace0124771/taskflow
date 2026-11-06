import time

from app.database import SessionLocal
from app import models
from app.queue import redis_client, QUEUE_NAME
from app.tasks import run_task


def process_one(job_id):
    db = SessionLocal()
    try:
        job = db.get(models.Job, job_id)
        if job is None:
            print(f"Job {job_id} not found in database, skipping")
            return
        print(f"Picked up job {job.id} ({job.task_type})")
        job.status = "running"
        job.attempts = job.attempts + 1
        db.commit()
        try:
            result = run_task(job.task_type, job.payload)
            job.status = "success"
            job.result = str(result)
            print(f"Job {job.id} succeeded with result: {result}")
        except Exception as error:
            job.status = "failed"
            job.result = str(error)
            print(f"Job {job.id} failed: {error}")
        db.commit()
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
