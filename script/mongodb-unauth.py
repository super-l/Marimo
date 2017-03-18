# coding=utf-8

"""
MongodDB未授权访问

"""

import pymongo



def poc(url):
    flag = "MongodDB unauth"
    ip = url
    port = 27017
    try:

        conn = pymongo.MongoClient(ip, port, socketTimeoutMS=3000)
        dbs = conn.database_names()
        if dbs:
            flag = ' -> ' + '|'.join(dbs)
            return [1,flag]
        else:
            return [0,flag]
    except Exception:
        return [0, flag]
