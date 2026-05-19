from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


from health_app.health import Health
from health_app.data import load_records, save_records

app = FastAPI(title="Health API")

class RecordIn(BaseModel):
    name: str
    weight_kg: float
    height_m: float

class RecordOut(BaseModel):
    name: str
    weight_kg: float
    height_m: float
    bmi: float
    category: str
    ideal_weight: float

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "app": "Health API"
    }

@app.get("/records", response_model=List[RecordOut])
def get_records():
    records = load_records()
    return records if records else []

@app.post("/records", response_model=RecordOut, status_code=201)
def create_record(record: RecordIn):
    try:
        person = Health(record.name, record.weight_kg, record.height_m)
        
        new_record = {
            "name": record.name,
            "weight_kg": record.weight_kg,
            "height_m": record.height_m,
            "bmi": round(person.bmi, 2),
            "category": person.get_category(),
            "ideal_weight": round(person.get_ideal_weight(), 1)
        }
        
        records = load_records()
        records.append(new_record)
        save_records(records)
        
        return new_record
        
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))