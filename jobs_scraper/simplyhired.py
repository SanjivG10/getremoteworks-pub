from bs4 import BeautifulSoup
from constant.constant import JOB_DATA
from utils import get_html,safe_get
from jobs_parser.main import Job
from typing import List

def get_job_link_from_page()->str:
    return JOB_DATA["simplyhired"]["link"] 


#  this has to be handled using puppeteer
def get_simplyhired_data(url,page=1)->List[Job]:
    html = get_html(url) 

    soup = BeautifulSoup(html,"html.parser")
    job_list= soup.select(JOB_DATA["simplyhired"]["selectors"]["job_list"])
    selectors = JOB_DATA["simplyhired"]["selectors"]["each_content"]

    jobs:List[Job] = []
    job_list= soup.select(JOB_DATA["simplyhired"]["selectors"]["job_list"])

    next_page =safe_get(soup.select(f'a[data-testid="paginationBlock{page+1}"]'),'href')

    for job in job_list:
        title = safe_get(job.select_one(selectors["title"]), 'text')
        link_element = job.select_one(selectors["link"])  
        link = link_element['href'] if link_element else None  
        company = safe_get(job.select_one(selectors["company"]), 'text')
        date_posted = safe_get(job.select_one(selectors["date_posted"]), 'text')
        description = safe_get(job.select_one(selectors["description"]), 'text')
        job = Job(title=title,company=company,date_posted=date_posted,link=link,description=description)

        jobs.append(job)

    return jobs,next_page

def get_all_simplyhired_data(MAX_PAGE=5)->List[Job]:
    data = []
    current_url  = get_job_link_from_page() 
    for page in range(1,MAX_PAGE+1):
        try:
            print("Trying",current_url)
            jobs,next = get_simplyhired_data(current_url,page)
            if not next:
                break
            current_url = next 
        except Exception as e:
            print(str(e))
        data.extend(jobs)
    return data



