import os
from typing import Optional
from json import JSONDecoder
from fastapi import FastAPI
from pymongo import MongoClient
from bson.json_util import dumps


client = MongoClient(os.environ.get("DB_HOST", '127.0.0.1'), os.environ.get("DB_PORT", 27017))
db = client.employees

app = FastAPI()


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Greetings!"}


@app.get("/get_employee/")
async def get(name: Optional[str] = None,
              company: Optional[str] = None,
              gender: Optional[str] = None,
              age: Optional[int] = None,
              salary: Optional[int] = None,
              job_title: Optional[str] = None):
    employee = db.employees
    find_params = {}
    if company is not None:
        find_params["company"] = company
    if name is not None:
        find_params["name"] = name
    if gender is not None:
        find_params["gender"] = gender
    if age is not None:
        find_params["age"] = age
    if salary is not None:
        find_params["salary"] = salary
    if job_title is not None:
        find_params["job_title"] = job_title
    mongo_data = employee.find(find_params)
    mongo_data = dumps(mongo_data)
    json_data = JSONDecoder().decode(mongo_data)
    return json_data
