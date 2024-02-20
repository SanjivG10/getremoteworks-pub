
from  pydantic import BaseModel
from typing import Optional,List

class Job(BaseModel):
    title: str = ""
    company: Optional[str] = ""
    date_posted: Optional[str] = ""
    description: Optional[str] = ""
    salary: Optional[str] = ""
    employmentType: Optional[str] = ""
    location: Optional[str] = ""
    link: Optional[str] = ""
    category: Optional[str] =""
    workHours: Optional[str] = ""
    benefits: Optional[List[str]] = ""
