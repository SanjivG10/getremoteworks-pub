from bs4 import BeautifulSoup
from constant.constant import JOB_DATA
from utils import get_html,safe_get,parse_relative_time
from constant.headers import simplyhired_headers
from jobs_parser.main import Job
from typing import List

def get_job_link_from_page()->str:
    return JOB_DATA["simplyhired"]["link"] 


#  this has to be handled using puppeteer
def get_simplyhired_data(url,page=1)->List[Job]:
    html = get_html(url,simplyhired_headers) 

    soup = BeautifulSoup(html,"html.parser")
    job_list= soup.select(JOB_DATA["simplyhired"]["selectors"]["job_list"])
    selectors = JOB_DATA["simplyhired"]["selectors"]["each_content"]

    jobs:List[Job] = []
    job_list= soup.select(JOB_DATA["simplyhired"]["selectors"]["job_list"])

    next_page_selector = f'a[data-testid="paginationBlock{page+1}"]'
    next_page =safe_get(soup.select_one(f'{next_page_selector}'),'href')

    for job in job_list:
        title = safe_get(job.select_one(selectors["title"]), 'text')
        link_element = job.select_one(selectors["link"])  
        link = link_element['href'] if link_element else None  
        company = safe_get(job.select_one(selectors["company"]), 'text')
        date_posted = parse_relative_time(safe_get(job.select_one(selectors["date_posted"]), 'text'))
        description = safe_get(job.select_one(selectors["description"]), 'text')
        job = Job(title=title,company=company,date_posted=date_posted,link=link,description=description,source='simplyhired')

        jobs.append(job)

    return jobs,next_page

def get_all_simplyhired_data(MAX_PAGE=5)->List[Job]:
    data = []
    current_url  = get_job_link_from_page() 
    for page in range(1,MAX_PAGE+1):
        try:
            jobs,next = get_simplyhired_data(current_url,page)
            data.extend(jobs)
            current_url = next 
            if not current_url:
                break
        except Exception as e:
            print(str(e))
    return data



