__author__ = 'luhaoliang'

import sys
from termcolor import colored

def banner():
    VERSION = '1.0'
    PROJECT = "Marimo"
    AUTHOR = 'S1mba'
    BANNER = """\033[01;34m
    ___  ___                 _
    |  \/  |                (_)                    \033[01;31m__/\033[01;34m
    | .  . |   __ _   _ __   _   _ __ ___     ___ \033[01;33m/ \033[01;31m__/\033[01;34m
    | |\/| |  / _` | | '__| | | | '_ ` _ \   / _ \ \033[01;33m_/\033[01;34m
    | |  | | | (_| | | |    | | | | | | | | | (_) |
    \_|  |_/  \__,_| |_|    |_| |_| |_| |_|  \___/
        \033[01;37m{\033[01;m Version %s by %s \033[01;37m}\033[0m
    \n""" % (VERSION, AUTHOR)

    sys.stdout.write(colored(BANNER, color=None, on_color=None, attrs=("bold",)))

