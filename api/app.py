from fastapi import FastAPI,UploadFile,File
from fastapi.responses import JSONResponse
import shutil
import os
import uuid
from src.pipeline.extractor_pipeline import run_extraction
app=FastAPI(title="Rental Agreement Extractor API")
UPLOAD_DIR="temp_uploads"
os.makedirs(UPLOAD_DIR,exist_ok=True)
@app.get("/")
def root():
    return {"message": "Rental Agreement API"}
@app.post("/extract")
async def extract_metadata(file:UploadFile=File(...)):
    file_id=str(uuid.uuid4())
    file_ext=os.path.splitext(file.filename)[1]
    file_path=os.path.join(UPLOAD_DIR,f"{file_id}{file_ext}")
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    try:
        result=run_extraction(file_path)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(status_code=500,content={"error":str(e)}) 
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)    