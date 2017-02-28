#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'luhaoliang'

from lib.core.data import paths,cmdLineOptions,conf,eg
from lib.utils.common import TARGET_MODE_STATUS
from lib.controller.api import runApi
import imp,os,Queue




def loadModule():
    if conf.SCRIPT_ALL:
        loadAllModule()
    else:
        eg.module_obj = imp.load_module('_',*imp.find_module(conf.MODULE_NAME,[paths.SCRIPT_PATH]))


#加载所有脚本
def loadAllModule():

    modules = []
    script_list = os.listdir(paths.MARIMO_ROOT_PATH + '/script')
    for script_name in script_list:
        if script_name.split('.')[1] == 'py':
            modules.append(script_name.split('.')[0])
    eg.module_list = modules


def loadTarget():

    eg.queue = Queue.Queue()

    if conf.TARGET_MODE is TARGET_MODE_STATUS.SINGLE:
        single_mode()

    elif conf.TARGET_MODE is TARGET_MODE_STATUS.FILE:
        file_mode()
    elif conf.TARGET_MODE is TARGET_MODE_STATUS.API:
        api_mode()




def single_mode():
    eg.queue.put(conf.TARGET_SINGLE)

def file_mode():
    for line in open(conf.INPUT_FILE_PATH):
        target = line.strip()
        if target:
            eg.queue.put(target)
def api_mode():
    conf.API_OUTPUT = os.path.join(paths.DATA_PATH, conf.API_MODE)
    if not os.path.exists(conf.API_OUTPUT):
        os.mkdir(conf.API_OUTPUT)

    file = runApi()
    for line in open(file):
        dest = line.strip()
        if dest:
            eg.queue.put(dest)

