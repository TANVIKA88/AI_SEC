from fastapi import FastAPI
from pathlib import Path
from dotenv import load_dotenv
from pypdf import PdfReader

app=FastAPI()

@app.get("/")
def home():
    return {"message": "Hello,hehe  World!"}