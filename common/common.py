#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: common.py
@time: 2019/1/23 17:12
@desc:
'''

def activation_hei_yu(adb):
    command = '-d shell sh /data/data/me.piebridge.brevent/brevent.sh'
    print('激活：' + command)
    print(adb.run(command))
