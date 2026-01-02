import csv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://shahbazgeu.github.io"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI()
jobs = []

@app.get("/jobs")
def get_jobs():
    return jobs

@app.post("/jobs")
def save_jobs(new_jobs: list):
    global jobs
    jobs = new_jobs
    return {"status": "ok"}

@app.post("/jobs/import-csv")
async def import_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files allowed")

    content = (await file.read()).decode("utf-8").splitlines()
    reader = csv.DictReader(content)

    imported = 0
    for row in reader:
        job = {
            "type": row["type"],
            "hour": int(row["hour"]),
            "start": int(row["start"]),
            "duration": int(row["duration"]),
            "network": row.get("network") or None
        }
        jobs.append(job)
        imported += 1

    return {"imported": imported}
