
from  pydantic import BaseModel
from typing import Optional,List,Any

class Job(BaseModel):
    title: str = ""
    company: Optional[str] = ""
    date_posted: Optional[str] = ""
    description: Optional[str] = ""
    salary: Optional[str] = ""
    employment_type: Optional[str] = ""
    location: Optional[str] = ""
    link: Optional[str] = ""
    category: Optional[str] =""
    workHours: Optional[str] = ""
    benefits: Optional[List[str]] = ""
    meta: Optional[Any]=None
