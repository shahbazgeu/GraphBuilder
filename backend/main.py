from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict
    allow_methods=["*"],
    allow_headers=["*"],
)

class Job(BaseModel):
    type: str
    hour: float
    start: int
    duration: int
    network: str | None = None

jobs: List[Job] = []

@app.get("/jobs")
def get_jobs():
    return jobs

@app.post("/jobs")
def save_jobs(new_jobs: List[Job]):
    global jobs
    jobs = new_jobs
    return {"status": "saved", "count": len(jobs)}
