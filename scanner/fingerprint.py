#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import urllib2
import random
from lib.core.data import paths

is_identification = False
g_index = 0




def request_url(url='', data=None, header={}):
    page_content = ''
    request = urllib2.Request(url, data, header)

    try:
        response = urllib2.urlopen(request)
        page_content = response.read()
    except Exception, e:
        pass

    return page_content

def scan(target):
    global is_identification
    global g_index
    global cms

    file = paths.DICT_PATH + '/cms.txt'
    f = open(file)
    cms = f.readlines()
    if target.endswith('/'):
        target = target[:-1]

    if target.startswith('http://') or target.startswith('https://'):
        pass
    else:
        target = 'http://' + target

    while True:
        if is_identification:
            break

        if g_index > len(cms)-1:
            break


        eachline = cms[g_index]
        g_index = g_index + 1


        if len(eachline.strip())==0 or eachline.startswith('#'):
            pass
        else:
            url, pattern, cmsname = eachline.split('------')
            html = request_url(target+url)
            rate = float(g_index)/float(len(cms))
            ratenum = int(100*rate)
            sys.stdout.write(random.choice('x+') + ' ' + str(ratenum) + '% ' + target+url +  "\r")
            sys.stdout.flush()

            if pattern.upper() in html.upper():
                is_identification = True
                print "[*] %s 成功识别CMS：%s，匹配的URL：%s，匹配的规则：%s" % (target,cmsname.strip('\n').strip('\r'), url, pattern)
                break
    return










