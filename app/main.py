from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database import get_db, engine, Base
from app import models
from app.schemas import JobCreate, JobRead

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow", description="A distributed job processing platform")


@app.get("/")
def read_root():
    return {"service": "TaskFlow", "message": "Welcome to the TaskFlow API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/jobs", response_model=JobRead, status_code=201)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    new_job = models.Job(task_type=job.task_type, payload=job.payload)
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job


@app.get("/jobs", response_model=list[JobRead])
def list_jobs(db: Session = Depends(get_db)):
    jobs = db.execute(select(models.Job).order_by(models.Job.id)).scalars().all()
    return jobs


@app.get("/jobs/{job_id}", response_model=JobRead)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.get(models.Job, job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
