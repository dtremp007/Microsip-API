from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.query import queryDatabase
from database.queryBuilder import selectBySku
from typing import Union
from settings import Settings

app = FastAPI()

origins = Settings["cors"]["origins"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/inventory/{sku}")
def get_items(sku: str):
    query = selectBySku(sku)
    return queryDatabase(query)
