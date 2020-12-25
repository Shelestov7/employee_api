from typing import Optional

from fastapi import FastAPI

from db.db import db
from models.models import Employee

app = FastAPI()


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Greetings!"}


@app.post("/get/")
def get(employee: Optional[Employee]):
    find_params = {}
    employees = []
    response_data = employee.dict()
    for key, value in response_data.items():
        if value is not None:
            find_params[key] = value
    for employe in db.employees.find(find_params):
        employees.append(Employee(**employe))
    print(find_params)
    return {"employees": employees}
