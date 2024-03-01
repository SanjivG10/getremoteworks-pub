import requests
import os
from jobs_parser.main import Job
from typing import List

url = "https://jsearch.p.rapidapi.com/search"


headers = {
	"X-RapidAPI-Key": os.getenv("RAPID_API_KEY") ,
	"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

def get_rapid_api_job(page:int):
    response = requests.get(url, headers=headers, params={
        "query":"Python Javascript React Node",
        "page":f"{page}",
        "num_pages":f"1",
        "date_posted":"week",
        "remote_jobs_only":True
    })
    data = response.json()

    jobs: List[Job] = []

    for each_job in data.get("data"):
        title = each_job["job_title"]
        link = each_job["job_apply_link"]
        # description = each_job["job_description"]
        date_posted = each_job["job_posted_at_timestamp"]
        source="rapidapi"
        company = each_job["employer_name"]
        job = Job(title=title,link=link,description="",date_posted=date_posted,source=source,company=company)
        jobs.append(job)

    return jobs

def get_all_rapid_api_keys(MAX_PAGES= 1):
    jobs_data:List[Job] = []
    for i in range(1,MAX_PAGES+1):
        try:
            jobs = get_rapid_api_job(i)
            jobs_data.extend(jobs)
        except:
            pass
    return jobs_data


