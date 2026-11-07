from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy import select, func

from app.database import get_db, engine, Base
from app import models
from app.schemas import JobCreate, JobRead
from app.queue import enqueue_job, redis_client, DEAD_LETTER_NAME

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow", description="A distributed job processing platform")


@app.get("/")
def read_root():
    return FileResponse("static/index.html")


@app.get("/dashboard")
def dashboard():
    return FileResponse("static/dashboard.html")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/jobs", response_model=JobRead, status_code=201)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    new_job = models.Job(task_type=job.task_type, payload=job.payload)
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    enqueue_job(new_job.id)
    return new_job


@app.get("/jobs", response_model=list[JobRead])
def list_jobs(status: str | None = None, db: Session = Depends(get_db)):
    query = select(models.Job).order_by(models.Job.id)
    if status is not None:
        query = query.where(models.Job.status == status)
    jobs = db.execute(query).scalars().all()
    return jobs


@app.get("/stats")
def job_stats(db: Session = Depends(get_db)):
    rows = db.execute(
        select(models.Job.status, func.count()).group_by(models.Job.status)
    ).all()
    counts = {row[0]: row[1] for row in rows}
    total = sum(counts.values())
    return {"total": total, "by_status": counts}


@app.get("/dead", response_model=list[JobRead])
def dead_letter(db: Session = Depends(get_db)):
    ids = redis_client.lrange(DEAD_LETTER_NAME, 0, -1)
    jobs = []
    for job_id in ids:
        job = db.get(models.Job, int(job_id))
        if job is not None:
            jobs.append(job)
    return jobs


@app.get("/jobs/{job_id}", response_model=JobRead)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.get(models.Job, job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
