#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: test_heiyu.py
@time: 2019/1/24 10:24
@desc:
'''


class heiyu():

    def __init__(self,adb_tools):
        self.adb_tools = adb_tools

    def run(self):
        command = '-d shell sh /data/data/me.piebridge.brevent/brevent.sh'
        print('激活：' + command)
        print(self.adb_tools.adb_run(command))