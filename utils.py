import requests
from constant.headers import headers

def get_html(url):
    html = requests.get(url,headers=headers).text
    return html 


def is_array(var):
    return isinstance(var,list)

def safe_get(element, attribute):
    try:
        if attribute == 'text':
            return element.text
        else:
            return element.get(attribute)
    except AttributeError:
        return ""
