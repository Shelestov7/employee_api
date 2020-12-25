from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field


class PyObjectId(ObjectId):

    validate = None

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objected')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class Employee(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    company: Optional[str] = None
    join_date: Optional[datetime] = None
    job_title: Optional[str] = None
    gender: Optional[str] = None
    salary: Optional[int] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
