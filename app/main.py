import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from fastapi import FastAPI
from app.routes import secure

app = FastAPI()

app.include_router(secure.router)

@app.get("/")
async def root():
    return {"message": "API rodando!"}
