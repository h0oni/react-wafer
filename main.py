from fastapi import FastAPI
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI()

class Post(BaseModel):
    img: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

f = open('wafermap.json')

wafermap = json.load(f)

@app.get('/')
async def hello():
    return {'hello':'world'}

@app.post('/wafermap/')
async def test():
    return wafermap
