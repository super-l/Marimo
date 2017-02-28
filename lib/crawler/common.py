__author__ = 'luhaoliang'

import requests

def download(url,user_agent='wssp'):
    headers = {'User-agent':user_agent}
    try:
        html = requests.get(url,headers=headers).text
    except:
        html = None

    return html

