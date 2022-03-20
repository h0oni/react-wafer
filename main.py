from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI()

# class Post(BaseModel):
#     emp_no: int = 44782
#     line_id: int = 24
#     seq_no: int = 3

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

f = open('wafermap.json')

wafermap = 'No file uploaded'

@app.get('/')
async def hello():
    global wafermap
    wafermap = 'No file uploaded'
    return {'hello':'world'}

@app.get('/wafermap/')
async def test():
    return wafermap

@app.post("/file/")
async def create_upload_file(file: UploadFile = File(...)):
    global wafermap, f
    wafermap = json.load(f)
    return {"filename": file.filename}

# @app.post("/test/")
# async def test(post:Post):
#     return post