import requests
from constant.headers import headers,monster_headers
from datetime import datetime,timedelta
import random
import string
import re
import dateparser

def generate_random_string(length:int)->str:
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def get_html(url,headers=headers):
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
    
def convert_to_date(date_str, year=None):
    date_formats = ["%d %b", "%b %d"]
    
    current_date = datetime.now().date()
    current_year = current_date.year
    
    if year is None:
        year = current_year
    
    for date_format in date_formats:
        try:
            full_date_str = f"{date_str} {year}"
            date_obj = datetime.strptime(full_date_str, f"{date_format} %Y").date()
            
            if date_obj > current_date:
                date_obj = datetime.strptime(f"{date_str} {year - 1}", f"{date_format} %Y").date()
            
            return date_obj
        except ValueError:
            continue  
    return None

def convert_date_str_to_date(date_str:str):
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")



def parse_relative_time(time_string):
    try:
        date_obj = dateparser.parse(time_string, settings={'PREFER_DATES_FROM': 'past'})
    except:
        pass 
    return date_obj



    

    

