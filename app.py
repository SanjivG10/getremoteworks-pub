from typing import List
from dotenv import load_dotenv
load_dotenv()

from db import post_jobs 

from jobs_scraper.remoteok import get_all_remote_ok_jobs
from jobs_scraper.weworkremotely import get_all_weworkremotely_data
from jobs_scraper.monster import get_all_monster_data 
from jobs_scraper.ziprecruiter import get_all_ziprecruiter_data
from jobs_scraper.simplyhired import get_all_simplyhired_data
from jobs_scraper.euremotejobs import get_all_euremotejobs_data
from jobs_scraper.rapidapi import get_all_rapid_api_keys

def post_all_jobs(companies:List[str]):
    if "monster" in companies:
        print("saving monster jobs")
        jobs = get_all_monster_data()
        print(f'Got {len(jobs)} jobs')
        post_jobs(jobs)

    if "simplyhired" in companies:
        print("saving simply hired jobs")
        jobs = get_all_simplyhired_data()
        print(f'Got {len(jobs)} jobs')
        post_jobs(jobs)

    if "euremotejobs" in companies:
        print("saving euremote jobs")
        jobs = get_all_euremotejobs_data()
        print(f'Got {len(jobs)} jobs')
        post_jobs(jobs)

    if "ziprecruiter" in companies:
        print("saving zip recruiter jobs")
        jobs = get_all_ziprecruiter_data()
        print(f'Got {len(jobs)} jobs')
        post_jobs(jobs)

    if "weworkremotely" in companies:
        print("saving we work remotely jobs")
        jobs = get_all_weworkremotely_data()
        print(f'Got {len(jobs)} jobs')
        post_jobs(jobs)

    if "remoteok" in companies:
        print("saving remote okay jobs")
        jobs = get_all_remote_ok_jobs()
        print(f'Got {len(jobs)} jobs')
        post_jobs(jobs)

    if "rapidapi" in companies:
        print("saving jobs from rapid api")
        jobs = get_all_rapid_api_keys()
        print(f'Got {len(jobs)} jobs')
        post_jobs(jobs)

print("Posting Jobs...")
companies = ["monster","rapidapi","remoteok","weworkremotely","ziprecruiter","euremotejobs"]
post_all_jobs(companies)













