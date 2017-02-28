__author__ = 'luhaoliang'

import os
import time
from lib.core.data import conf
from lib.utils.common import API_MODE_NAME
from lib.api.zoomeye.pack import ZoomeyeSearch

def runApi():
    output = conf.API_OUTPUT
    dork = conf.API_DORK
    limit = conf.API_LIMIT
    if conf.API_MODE is API_MODE_NAME.ZOOMEYE:
        anslist = ZoomeyeSearch(query=dork, limit=limit, type=conf.ZOOMEYE_SEARCH_TYPE)
    tmpIpFile = os.path.join(output, '%s.txt' % (time.strftime('%Y%m%d%H%M%S')))
    with open(tmpIpFile, 'w+') as fp:
        for each in anslist:
            if isinstance(each, list):  # for ZoomEye web type
                each = each[0]
            fp.write(each + '\n')
    return tmpIpFile

