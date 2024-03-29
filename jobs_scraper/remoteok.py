from bs4 import BeautifulSoup
from constant.constant import JOB_DATA
import json
from utils import get_html,is_array
from jobs_parser.main import Job
from typing import List

def get_job_link_from_page(page:int)->str:
    return JOB_DATA["remote_ok"]["link"] + str(page*10)

def get_remote_ok_data(url:str)->List[Job]:
    html = get_html(url) 
    soup = BeautifulSoup(html,"html.parser")
    job_list= soup.find_all(JOB_DATA["remote_ok"]["selectors"]["job_list"])

    jobs:List[Job] = []

    for job in job_list:
        data = (job.find('script', type='application/ld+json'))
        link_tag = job.find("a")
        if data:
            link = link_tag["href"] if link_tag else ""
            data =json.loads(data.text)
            title = data.get("title")
            company = data.get("hiringOrganization").get("name")

            date_posted = data.get("datePosted")

            base_salary = data.get("baseSalary")

            salary = f'{base_salary.get("currency")}{base_salary.get("value").get("minValue")}-{base_salary.get("value").get("minValue")}'

            employment_type = data.get("employment_type")

            location_requirement = data.get("applicantLocationRequirements")

            if (is_array(location_requirement)):
                location = ", ".join(list(map(lambda x: x.get("name"),location_requirement)))
            else:
                location = location_requirement.get("name")
            workHours = data.get("workHours")

            job = Job(title=title,company=company,date_posted=date_posted,description="",salary=salary,employment_type=employment_type,location=location,workHours=workHours,benefits="",link=link,source="remoteok")

            jobs.append(job)
    return jobs 

def get_all_remote_ok_jobs()->List[Job]:
    data = []
    pages = ["https://remoteok.com/remote-nodejs-jobs","https://remoteok.com/remote-dev-jobs","https://remoteok.com/remote-backend-jobs","https://remoteok.com/remote-react-jobs","https://remoteok.com/remote-full-stack-jobs"]
    for page in pages:
        try:
            jobs = get_remote_ok_data(page)
            data.extend(jobs)
        except Exception as e:
            print(str(e))

    return data
