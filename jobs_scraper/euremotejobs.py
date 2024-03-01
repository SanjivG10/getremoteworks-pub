from bs4 import BeautifulSoup
from constant.constant import JOB_DATA
from utils import safe_get,get_post_data,parse_relative_time
from jobs_parser.main import Job
from typing import List
from constant.headers import euremotejobs_headers 
from test import get_job

def get_job_link_from_page()->str:
    return JOB_DATA["euremotejobs"]["link"] 

def get_euremotejobs_data(url,page=1)->List[Job]:
    data = {
    'lang': '',
    'search_keywords': '',
    'search_location': '',
    'filter_job_type[]': [
        '4-day-week',
        'ai',
        'bilingual',
        'dutch',
        'freelance',
        'french',
        'full-time',
        'german',
        'internship',
        'italian',
        'jobs-in-crypto',
        'part-time',
        'portuguese',
        'russian',
        'spanish',
        'temporary',
        'web3',
        '',
    ],
    'per_page': '20',
    'orderby': 'featured',
    'featured_first': 'false',
    'order': 'DESC',
    'page': '1',
    'show_pagination': 'false',
    'form_data': 'search_keywords=&search_region=0&job_tag%5B%5D=Python&job_tag%5B%5D=Typescript&job_tag%5B%5D=React&job_tag%5B%5D=NodeJS&job_tag%5B%5D=ReactJS&job_tag%5B%5D=MongoDB&filter_job_type%5B%5D=4-day-week&filter_job_type%5B%5D=ai&filter_job_type%5B%5D=bilingual&filter_job_type%5B%5D=dutch&filter_job_type%5B%5D=freelance&filter_job_type%5B%5D=french&filter_job_type%5B%5D=full-time&filter_job_type%5B%5D=german&filter_job_type%5B%5D=internship&filter_job_type%5B%5D=italian&filter_job_type%5B%5D=jobs-in-crypto&filter_job_type%5B%5D=part-time&filter_job_type%5B%5D=portuguese&filter_job_type%5B%5D=russian&filter_job_type%5B%5D=spanish&filter_job_type%5B%5D=temporary&filter_job_type%5B%5D=web3&filter_job_type%5B%5D='}

    job_res = get_post_data(url,data=data,headers=euremotejobs_headers,use_data=True) 
    html = job_res["html"]
    soup = BeautifulSoup(html,"html.parser")
    job_list= soup.select(JOB_DATA["euremotejobs"]["selectors"]["job_list"])
    selectors = JOB_DATA["euremotejobs"]["selectors"]["each_content"]

    jobs:List[Job] = []

    if page > job_res["max_num_pages"]:
        return jobs

    for job in job_list:
        title = safe_get(job.select_one(selectors["title"]), 'text')
        link_element = job.select_one(selectors["link"])  
        link = link_element['href'] if link_element else None  
        company = safe_get(job.select_one(selectors["company"]), 'text')
        location = safe_get(job.select_one(selectors["location"]), 'text')
        date_posted = parse_relative_time(safe_get(job.select_one(selectors["date_posted"]), 'text').replace("Posted","").strip())
        employment_type = safe_get(job.select_one(selectors["employment_type"]), 'text')
        job = Job(title=title,company=company,date_posted=date_posted,link=link,employment_type=employment_type,location=location,source="euremotejobs")
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






