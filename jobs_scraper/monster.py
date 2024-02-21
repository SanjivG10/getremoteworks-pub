from constant.constant import JOB_DATA
from utils import get_post_data
from jobs_parser.main import Job
from typing import List
from utils import monster_headers

api_key = "AE50QWejwK4J73X1y1uNqpWRr2PmKB3S"

def get_job_link_from_page()->str:
    return JOB_DATA["monster"]["link"]+api_key

def get_monster_current_page_data(page:int)->List[Job]:
    url = get_job_link_from_page()

    json_data = {
    'jobQuery': {
        'query': '',
        'locations': [
            {
                'country': 'us',
                'address': 'remote',
                'radius': {
                    'unit': 'mi',
                    'value': 20,
                },
            },
        ],
    },
    'jobAdsRequest': {
        'position': [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
        ],
        'placement': {
            'channel': 'MOBILE',
            'location': 'JobSearchPage',
            'property': 'monster.com',
            'type': 'JOB_SEARCH',
            'view': 'CARD',
        },
    },
    'fingerprintId': 'z3a361ed2a2c39bb39c8cbfc3df24edd6',
    'offset': 9*page,
    'pageSize': 9,
    'includeJobs': [],
    }

    data = get_post_data(url,data=json_data,headers=monster_headers)
    jobs:List[Job] = []

    for each_job in data["jobResults"]:
        job_posting = each_job["jobPosting"]
        url = job_posting["url"]

        title = job_posting["title"]
        company =  job_posting["hiringOrganization"]["name"]
        date_posted = job_posting["datePosted"]
        description = job_posting["description"]
        link= job_posting["url"]
        job = Job(title=title,company=company,date_posted=date_posted,description=description,link=link,meta=each_job)
        jobs.append(job)

    return jobs 

def get_all_monster_data(MAX_PAGE=5):
    jobs_data:List[Job] = []
    for page in range(MAX_PAGE):
        try:
            jobs = get_monster_current_page_data(page)
            jobs_data.extend(jobs)
        except Exception as e:
            print(e)
        return jobs_data
    

