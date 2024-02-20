import requests
from constant.headers import headers,monster_headers

import random
import string

def generate_random_string(length:int)->str:
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def get_html(url):
    html = requests.get(url,headers=headers).text
    return html 

def get_post_data(url,data,headers=monster_headers):
    data = requests.post(url,json=data,headers=headers)
    return data.json()

def is_array(var):
    return isinstance(var,list)

def safe_get(element, attribute):
    try:
        if attribute == 'text':
            return element.text.strip()
        else:
            return element.get(attribute).strip()
    except AttributeError:
        return ""
    

