import requests
from constant.headers import euremotejobs_headers

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
    'form_data': 'search_keywords=&search_region=0&job_tag%5B%5D=Python&job_tag%5B%5D=Typescript&job_tag%5B%5D=React&job_tag%5B%5D=NodeJS&job_tag%5B%5D=ReactJS&job_tag%5B%5D=MongoDB&filter_job_type%5B%5D=4-day-week&filter_job_type%5B%5D=ai&filter_job_type%5B%5D=bilingual&filter_job_type%5B%5D=dutch&filter_job_type%5B%5D=freelance&filter_job_type%5B%5D=french&filter_job_type%5B%5D=full-time&filter_job_type%5B%5D=german&filter_job_type%5B%5D=internship&filter_job_type%5B%5D=italian&filter_job_type%5B%5D=jobs-in-crypto&filter_job_type%5B%5D=part-time&filter_job_type%5B%5D=portuguese&filter_job_type%5B%5D=russian&filter_job_type%5B%5D=spanish&filter_job_type%5B%5D=temporary&filter_job_type%5B%5D=web3&filter_job_type%5B%5D=',
}

def get_job():
    response = requests.post('https://euremotejobs.com/jm-ajax/get_listings/', headers=euremotejobs_headers, data=data)
    return response.json()
