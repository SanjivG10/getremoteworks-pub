
from  pydantic import BaseModel
from typing import Optional,List,Any
from datetime import  datetime


class Job(BaseModel):
    title: str = ""
    company: Optional[str] = ""
    date_posted: Optional[datetime] = None
    description: Optional[str] = ""
    salary: Optional[str] = ""
    source: Optional[str] = ""
    employment_type: Optional[str] = ""
    location: Optional[str] = ""
    link: Optional[str] = ""
    category: Optional[str] =""
    workHours: Optional[str] = ""
    benefits: Optional[str] = ""
    meta: Optional[Any]=None
