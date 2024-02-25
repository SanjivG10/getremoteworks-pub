from pymongo import MongoClient
import os 
import json
from typing import List 
from jobs_parser.main import Job

MONGO_URL = os.getenv("MONGODB_URL")

client = MongoClient(MONGO_URL)

db = client.getremoteworks

collection = db.Job

# filter = {'source': 'ziprecruiter'}
# collection.delete_many(filter)

def post_jobs(jobs:List[Job]):
    jobs = [json.loads(job.model_dump_json()) for job in jobs]
    for job in jobs:
        filter = {
            'link': job['link'],
            'source': job['source']
        }
        update = {
            '$set':job 
        }
        collection.update_one(filter, update, upsert=True)





