from jobs_scraper.remoteok import get_remote_ok_data
from jobs_scraper.weworkremotely import get_weworkremotely_data


jobs = get_weworkremotely_data()

for job in jobs:
    print(job.model_dump_json())
