__author__ = 'luhaoliang'
import os
from lib.core.data import paths,cmdLineOptions,conf,eg

def setPath():
    root_path = paths.MARIMO_ROOT_PATH
    paths.DATA_PATH = os.path.join(root_path, "data")
    paths.SCRIPT_PATH = os.path.join(root_path, "script")
    paths.OUTPUT_PATH = os.path.join(root_path, "output")

def target2hp(target):
    l = target.split(':')
    host = l[0]
    port = int(l[1])
    return host,port

class TARGET_MODE_STATUS:
    FILE = 9
    SINGLE = 8
    IPMASK = 7
    RANGE = 6
    API = 5


class ENGINE_MODE_STATUS:
    THREAD = 9
    GEVENT = 8


class API_MODE_NAME:
    ZOOMEYE = 'zoomeye'
    SHODAN = 'shodan'
    GOOGLE = 'google'