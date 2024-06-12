import os
from fastapi import FastAPI, UploadFile, File
from pathlib import Path
from datetime import datetime

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    today = datetime.now().strftime('%Y%m%d')
    folder_path = Path(f"/uploaded/{today}")
    if not folder_path.exists():
        os.mkdir(folder_path)

    file_location = folder_path / Path(file.filename).name
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"msg": f"file '{file.filename}' saved"}