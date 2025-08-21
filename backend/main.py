from fastapi import FastAPI, UploadFile
from backend import ipfs_utils, fhir_processor

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile):
    content = await file.read()
    cid = ipfs_utils.store_file(content)
    return {"ipfs_hash": cid}

@app.post("/fhir/process")
async def process_fhir(data: dict):
    result = fhir_processor.process_fhir_data(data)
    return {"processed": result}
