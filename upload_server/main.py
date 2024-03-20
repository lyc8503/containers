from fastapi import FastAPI, UploadFile, File
from pathlib import Path

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = Path("/uploaded") / Path(file.filename).name
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"msg": f"file '{file.filename}' saved"}