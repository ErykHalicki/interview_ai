from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)
class InterviewData(BaseModel):
    job_description: str = None
    resume: str = None
    cover_letter: str = None
    interview_type: str
    responses: str

@app.post("/submit_interview/")
async def submit_interview(data: InterviewData):
    # Here, you can process the interview data, store it in a database, etc.
    # For now, we'll just print it and return a dummy response
    print(data)
    return {"status": "success", "message": "Interview data processed"}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Interview API"}
