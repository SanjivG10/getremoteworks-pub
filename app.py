from jobs_scraper.remoteok import get_all_remote_ok_jobs 
from jobs_scraper.weworkremotely import get_weworkremotely_data
from jobs_scraper.monster import get_all_monster_data 
from jobs_scraper.ziprecruiter import get_all_ziprecruiter_data,get_ziprecruiter_data
from jobs_scraper.simplyhired import get_all_simplyhired_data

for job in get_all_simplyhired_data(2):
    print(job.model_dump_json())
