import json
from fastapi import FastAPI, HTTPException
from functions import searchHeight, searchWeight

app = FastAPI()

with open("./hw.json") as hw:
    hwd = json.load(hw)

@app.post("/height")
async def height(data: dict):
    try:
        result = searchHeight(data["gender"], data["height"], hwd)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/weight")
async def weight(data: dict):
    try:
        result = searchWeight(data["gender"], data["weight"], hwd)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
