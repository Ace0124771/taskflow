from fastapi import FastAPI

app = FastAPI(title="TaskFlow", description="A distributed job processing platform")


@app.get("/")
def read_root():
    return {"service": "TaskFlow", "message": "Welcome to the TaskFlow API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
