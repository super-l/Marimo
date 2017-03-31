__author__ = 'luhaoliang'

import requests

def download(url,user_agent='Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0'):
    headers = {'User-agent':user_agent}
    try:
        html = requests.get(url,headers=headers).text
    except:
        html = None

    return html

