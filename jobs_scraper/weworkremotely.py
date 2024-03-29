from bs4 import BeautifulSoup
from constant.constant import JOB_DATA
from utils import get_html,safe_get,convert_to_date
from jobs_parser.main import Job
from typing import List

def get_job_link_from_page()->str:
    return JOB_DATA["weworkremotely"]["link"] 

def get_all_weworkremotely_data()->List[Job]:
    url = get_job_link_from_page()
    html = get_html(url) 
    soup = BeautifulSoup(html,"html.parser")
    selectors = JOB_DATA["weworkremotely"]["selectors"]["each_content"]
    jobs:List[Job] = []
    job_list= soup.select(JOB_DATA["weworkremotely"]["selectors"]["job_list"])

    accepted_jobs_category = ["Full-Stack Programming Jobs","Front-End Programming Jobs","Back-End Programming Jobs"]

    for article in soup.select(JOB_DATA["weworkremotely"]["selectors"]["main_container"]):
        category = safe_get(article.select_one(selectors["category"]), 'text')
        if category not in accepted_jobs_category:
            continue

        for job in job_list:
            title = safe_get(job.select_one(selectors["title"]), 'text')
            company = safe_get(job.select_one(selectors["company"]), 'text')
            employment_type = safe_get(job.select_one(selectors["employment_type"]), 'text')
            location = safe_get(job.select_one(selectors["location"]), 'text')
            date_posted = convert_to_date(safe_get(job.select_one(selectors["date_posted"]), 'text'))
            if not date_posted:
                continue 
            link_element = job.select_one(selectors["link"])  
            link = link_element['href'] if link_element else None  
            job = Job(title=title,company=company,date_posted=date_posted,employment_type=employment_type,location=location,link=link,category=category,source="weworkremotely")


            jobs.append(job)

    return jobs 
