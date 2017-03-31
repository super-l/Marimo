#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'luhaoliang'

import os
from lib.parse.cmdline import cmdLineParser
from lib.core.option import initOptions
from lib.utils.settings import banner
from lib.utils.common import setPath
from lib.core.data import paths,cmdLineOptions,conf,eg
from lib.controller.controller import run
from lib.controller.loader import loadModule,loadTarget,loadScaner






def main():
    paths.MARIMO_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    setPath()
    cmdLineOptions.update(cmdLineParser().__dict__)
    #cmdLineParser()获得命令行参数，以字典返回给cmdLineOptions对象
    initOptions(cmdLineOptions)
    banner()
    loadModule()
    loadTarget()
    loadScaner()
    run()


if __name__ == "__main__":
    main()







