#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cmd
import subprocess
from lib.utils import logger
from lib.utils.plugin_manager import PluginManager
from lib.controller.controller import run
from lib.controller.loader import loadModule,loadTarget,loadScaner



class Interface(cmd.Cmd, PluginManager):

    def __init__(self):
        cmd.Cmd.__init__(self)
        PluginManager.__init__(self)
        self.prompt = "Marimo漏洞探测系统 (press \"q\" to re_scan) > "

    def do_help(self, line):
        """
        帮助
        :return:
        """
        commands = {
            "help": "帮助菜单",
            "version": "显示Marimo漏洞探测系统概况",
            "list_script": "列出所有内置漏洞探测脚本",
            "-s [--script]": "加载漏洞探测脚本",
            "-A": "加载所有漏洞探测脚本",
            "-sc [--scanner]": "加载漏洞扫描脚本",
            "-tS": "目标来自单一URL",
            "-tF": "目标来自文件",
            "-nZ": "目标来自ZoomEye (e.g. \"solr country:cn\")",
            "--limit": "从ZoomEye加载的最大目标数目",
            "-tC": "目标来自爬虫",
            "-cm": "爬虫最大爬取url个数",
            "-th": "线程数目",
            "-eT": "启动多线程（默认）",
            "-eG": "启动协程",
            "scan": "启动Marimo漏洞探测系统",
            "shell": "执行系统命令",
            "q":"重新设置参数以开始漏洞探测"
        }
        print "\nCore Commands\n=============\n"
        print "%-30s%s" % ("Command", "Description")
        print "%-30s%s" % ("-------", "-----------")
        for command in commands:
            print "%-30s%s" % (command, commands[command])
        print

    def do_version(self, line):
        """
        版本信息
        :return:
        """
        print
        print "Version: %s" % self.version()
        print "Scripts: %d" % self.script_num()
        print "Scanners: %d" % self.scanner_num()

    def do_list_script(self, line):
        """
        漏洞探测插件列表

        """
        print "\nDetect Plugins\n=======\n"
        print "%-40s%-40s" % ("Script_Name","Description")
        print "%-40s%-40s" % ("----", "-----")
        for script_name, description in self.list_script():
            print "%-40s%-40s" % (script_name, description)
        print
    def do_list_scanner(self, line):
        """
        漏洞扫描插件列表

        """
        print "\nScan Plugins\n=======\n"
        print "%-40s%-40s" % ("Scanner_Name","Description")
        print "%-40s%-40s" % ("----", "-----")
        for scanner_name, description in self.list_scanner():
            print "%-40s%-40s" % (scanner_name, description)
        print


    def do_scan(self,line):
        loadModule()
        loadTarget()
        loadScaner()
        run()


    def do_shell(self, arg):
        """
        执行系统命令
        :param arg:
        :return:
        """
        logger.process("exec: %s" % arg)
        sub_cmd = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
        print
        print sub_cmd.communicate()[0],

    def default(self, line):
        """
        无法识别命令时
        :param line:
        :return:
        """
        logger.error("Unknown command: %s" % line)

    def do_q(self, line):
        """
        退出
        :return:
        """
        self.exit()
        exit()

    def emptyline(self):
        """
        空行
        :return:
        """
        pass
