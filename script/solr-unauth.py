#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'luhaoliang'

"""
Apache Solr 未授权访问PoC
  (iterate_path函数使用场景示例)


"""

import requests
import urlparse



def poc(target):
    flag = "solr-unauth vulnerable"
    base_url = target if "://" in target else 'http://' + target
    for each in iterate_path(base_url):
        try:
            url = each
            g = requests.get(url, headers={'User-Agent': firefox()})
            if g.status_code is 200 and 'Solr Admin' in g.content and 'Dashboard' in g.content:
                return [1,flag]
            url = url + '/solr/'
            g = requests.get(url, headers={'User-Agent': firefox()})
            if g.status_code is 200 and 'Solr Admin' in g.content and 'Dashboard' in g.content:
                return [1,flag]
        except Exception:
            pass
    return [0,flag]

def firefox():
    return 'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0'
def get_domain(url):
    p = urlparse.urlparse(url)
    return urlparse.urlunsplit([p.scheme, p.netloc, '', '', ''])

def iterate_path(ori_str):

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