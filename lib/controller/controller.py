__author__ = 'luhaoliang'

import threading,time,os,imp
from lib.core.data import paths,cmdLineOptions,conf,eg

def initEngine():
    eg.module_name = conf.MODULE_NAME
    eg.thread_count = eg.thread_num = conf.THREAD_NUM
    setThreadLock()


def scan():
    while 1:
        eg.load_lock.acquire()
        if eg.queue.qsize() > 0:
            target = str(eg.queue.get(timeout=1.0))
            eg.load_lock.release()
        else:
            eg.load_lock.release()
            break

        if conf.SCRIPT_ALL:
            for scrip_name in eg.module_list:
                try:
                    module_obj = imp.load_module('_',*imp.find_module(scrip_name.split('.')[0],[paths.SCRIPT_PATH]))
                    status,vul = module_obj.poc(target)
                    resultHandler(status,vul,target)
                except:
                    pass
        else:
            try:
                status,vul = eg.module_obj.poc(target)
                resultHandler(status,vul,target)
            except:
                pass


    changeThreadCount(-1)








def run():
    initEngine()
    for i in range(eg.thread_num):
        t = threading.Thread(target=scan,name=str(i))
        t.daemon = True
        t.start()
    while 1:
        if eg.thread_count > 0:
            time.sleep(0.01)
        else:
            break


def setThreadLock():
    eg.load_lock = threading.Lock()
    eg.thread_count_lock = threading.Lock()


def changeThreadCount(num):
    eg.thread_count_lock.acquire()
    eg.thread_count += num
    eg.thread_count_lock.release()

def resultHandler(status,vul,target):
    if status:
        print target + " is " + vul
    else:
        print target + " is not " + vul


