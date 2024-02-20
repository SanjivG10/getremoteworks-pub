from bs4 import BeautifulSoup
from constant.constant import JOB_DATA
import json
from utils import get_html,safe_get
from jobs_parser.main import Job
from typing import List

def get_job_link_from_page(page:int)->str:
    return JOB_DATA["ziprecruiter"]["link"] + str(page)

def get_ziprecruiter_data(page=1)->List[Job]:
    url = get_job_link_from_page(page)
    html = get_html(url) 
    soup = BeautifulSoup(html,"html.parser")
    job_list= soup.select(JOB_DATA["ziprecruiter"]["selectors"]["job_list"])
    selectors = JOB_DATA["ziprecruiter"]["selectors"]["each_content"]

    jobs:List[Job] = []
    job_list= soup.select(JOB_DATA["ziprecruiter"]["selectors"]["job_list"])

    for job in job_list:
        title = safe_get(job.select_one(selectors["title"]), 'text')
        link_element = job.select_one(selectors["link"])  
        link = link_element['href'] if link_element else None  
        company = safe_get(job.select_one(selectors["company"]), 'text')
        location = safe_get(job.select_one(selectors["location"]), 'text')
        date_posted = safe_get(job.select_one(selectors["date_posted"]), 'text')
        description = safe_get(job.select_one(selectors["description"]), 'text')
        job = Job(title=title,company=company,date_posted=date_posted,location=location,link=link,description=description)

        jobs.append(job)

    return jobs 

def get_all_ziprecruiter_data(MAX_PAGE=5)->List[Job]:
    data = []
    for page in range(MAX_PAGE):
        try:
            jobs = get_ziprecruiter_data(page)
        except Exception as e:
            print(str(e))
        data.extend(jobs)
    return data

