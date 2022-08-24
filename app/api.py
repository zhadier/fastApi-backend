from fastapi import FastAPI
from functools import lru_cache
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

@lru_cache()
def cached_dotenv():
  load_dotenv()

cached_dotenv()

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/company-accounts")
async def read_root() -> dict:
    return {
    "fields": {
      "Account": "Intercom",
      "External_id ": "ATY67YT789",
      "Phone Number": "(510) 592-6600",
      "Company Size": "1-10",
      "MRR": 400,
      "Total signals": 32,
      "Assigned CSM name": "John Doe",
      "Assigned CSM email": "john@csm.com",
      "Segments": [
        "Mid Market",
        "B2B"
      ],
      "Company Logo": "https://logo.clearbit.com/intercom.io",
      "Website": "https://intercom.io",
      "Renewal date ": "2022-10-13",
      "Applied View": [
        "Renewal upcoming"
      ]
    }
  ,}