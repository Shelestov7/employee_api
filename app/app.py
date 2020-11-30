from typing import Optional

import uvicorn
from fastapi import FastAPI
from bson.json_util import dumps
from db.db import db
from db.models import Employee

app = FastAPI()


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Greetings!"}


@app.get("/get/")
def get(employee: Employee):
    find_params = {}
    response_data = employee.dict()
    for key, value in response_data.items():
        if value is not None:
            find_params[key] = value
    data = db.employees.find_one(find_params)
    print(find_params)
    return {"data": data}

