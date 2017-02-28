__author__ = 'luhaoliang'

from lib.api.zoomeye.base import Zoomeye


def _initial():
    z = Zoomeye()
    z.autologin()
    info = z.resource_info()['resources']
    if info:
        msg = 'Available ZoomEye search: (web:%s,host:%s)' % (info['web-search'], info['host-search'])
        print msg
    else:
        msg = 'ZoomEye API authorization failed, Please re-run it and enter a new token.'
        print msg

    return z

def ZoomeyeSearch(query,limit,type='host',offset=0):
    z = _initial()
    ans = []
    limit += offset
    for page in range(int(offset / 10), int((limit + 10 - 1) / 10)):
        data = z.dork_search(query, resource=type, page=page)
        if data:
            for i in data:
                ip_str = i.get('ip')
                if 'portinfo' in i:
                    ip_str = ip_str + ':' + str(i.get('portinfo').get('port'))
                ans.append(ip_str)

        else:
            break
    return ans


