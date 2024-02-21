from bs4 import BeautifulSoup
from constant.constant import JOB_DATA
from utils import safe_get,get_post_data
from jobs_parser.main import Job
from typing import List

def get_job_link_from_page()->str:
    return JOB_DATA["euremotejobs"]["link"] 

def get_euremotejobs_data(url,page=1)->List[Job]:
    data = {
    'lang': '',
    'search_keywords': '',
    'search_location': '',
    'per_page': '20',
    'orderby': 'featured',
    'featured_first': 'false',
    'order': 'DESC',
    'page': f'{page}',
    'show_pagination': 'false'}
    job_res = get_post_data(url,data=data) 
    html = job_res["html"]
    soup = BeautifulSoup(html,"html.parser")
    job_list= soup.select(JOB_DATA["euremotejobs"]["selectors"]["job_list"])
    selectors = JOB_DATA["euremotejobs"]["selectors"]["each_content"]

    jobs:List[Job] = []

    for job in job_list:
        title = safe_get(job.select_one(selectors["title"]), 'text')
        link_element = job.select_one(selectors["link"])  
        link = link_element['href'] if link_element else None  
        company = safe_get(job.select_one(selectors["company"]), 'text')
        location = safe_get(job.select_one(selectors["location"]), 'text')
        date_posted = safe_get(job.select_one(selectors["date_posted"]), 'text').replace("Posted","").strip()
        employment_type = safe_get(job.select_one(selectors["employment_type"]), 'text')
        job = Job(title=title,company=company,date_posted=date_posted,link=link,employment_type=employment_type,location=location)
        jobs.append(job)

    return jobs

def get_all_euremotejobs_data(MAX_PAGE=5)->List[Job]:
    data = []
    current_url  = get_job_link_from_page() 
    for page in range(1,MAX_PAGE+1):
        try:
            jobs = get_euremotejobs_data(current_url,page)
            data.extend(jobs)
        except Exception as e:
            print(str(e))
    return data



