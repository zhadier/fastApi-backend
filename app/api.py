from fastapi import FastAPI
from functools import lru_cache
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from .airtable import Airtable

@lru_cache()
def cached_dotenv():
  load_dotenv()

cached_dotenv()

AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = os.environ.get("AIRTABLE_TABLE_NAME")


app = FastAPI()

origins = [
    "http://localhost:3001",
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
    airtable_client = Airtable(base_id=AIRTABLE_BASE_ID, api_key=AIRTABLE_API_KEY,table_name=AIRTABLE_TABLE_NAME)
    return airtable_client.get_companies()
  