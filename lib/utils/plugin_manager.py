#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sqlite3



class PluginManager(object):
    """
    插件管理器
    """
    def __init__(self):
        self.plugins = {}
        self.conn = sqlite3.connect("database/core.db")
        self.conn.text_factory = str
        self.cu = self.conn.cursor()
        self.current_plugin = ""

    def list_script(self):
        self.cu.execute("select script_name, description from script")
        return self.cu.fetchall()

    def list_scanner(self):
        self.cu.execute("select scanner_name, description from scanner")
        return self.cu.fetchall()

    def version(self):
        """
        插件库版本
        :return: string, 插件库版本
        """
        self.cu.execute("select version from core")
        return self.cu.fetchone()[0]


    def script_num(self):
        """
        查询漏洞探测插件数量
        :return: int, 插件数量
        """
        self.cu.execute("select count(*) from script")
        return self.cu.fetchone()[0]
    def scanner_num(self):
        """
        查询漏洞扫描插件数量
        :return: int, 插件数量
        """
        self.cu.execute("select count(*) from scanner")
        return self.cu.fetchone()[0]

    def exit(self):
        """
        退出插件管理器
        :return:
        """
        self.conn.close()
