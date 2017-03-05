__author__ = 'luhaoliang'

from lib.core.data import paths,cmdLineOptions,conf,eg
from lib.utils.common import TARGET_MODE_STATUS,API_MODE_NAME,ENGINE_MODE_STATUS

import os


def initOptions(args):
    engineRegister(args)
    moduleRegister(args)
    targetRegister(args)
    apiRegister(args)

def engineRegister(args):
    if args.engine_gevent:
        conf.ENGINE = ENGINE_MODE_STATUS.GEVENT
    else:
        conf.ENGINE = ENGINE_MODE_STATUS.THREAD
    conf.THREAD_NUM = args.thread_num

def moduleRegister(args):
    conf.MODULE_NAME = args.script_name
    conf.SCRIPT_ALL =args.all_script


def targetRegister(args):
    input_single = args.target_single
    input_file = args.target_file
    api_zoomeye = args.zoomeye_dork

    def file():
        conf.TARGET_MODE = TARGET_MODE_STATUS.FILE
        conf.INPUT_FILE_PATH = input_file
    def single():
        conf.TARGET_MODE = TARGET_MODE_STATUS.SINGLE
        conf.TARGET_SINGLE = input_single

    def zoomeye():
        conf.TARGET_MODE = TARGET_MODE_STATUS.API
        conf.API_MODE = API_MODE_NAME.ZOOMEYE
        conf.API_DORK = api_zoomeye

    if input_file:
        file()
    elif input_single:
        single()
    elif api_zoomeye:
        zoomeye()

def apiRegister(args):
    search_type = args.search_type
    api_limit = args.api_limit
    if not 'API_MODE' in conf:
        return
    if not conf.API_DORK:
        msg = 'Empty API dork, show usage with [-h]'
        print msg

    if api_limit <= 0:
        msg = 'Invalid value in [--limit], show usage with [-h]'
        print msg
    else:
        conf.API_LIMIT = api_limit
    if conf.API_MODE is API_MODE_NAME.ZOOMEYE:
        if search_type not in ['web', 'host']:
            msg = 'Invalid value in [--search-type], show usage with [-h]'
            print msg
        else:
            conf.ZOOMEYE_SEARCH_TYPE = search_type





