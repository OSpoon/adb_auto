#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: test_wechar.py
@time: 2019/1/24 10:30
@desc:
'''
import random

import xmltodict


class wechar():

    def __init__(self,adb_tools):
        self.adb_tools = adb_tools

    def analysis(self, obj):
        if isinstance(obj, dict):

            if obj['@text'] == '添加为熟朋友':
                x1 = float(obj['@bounds'].split('][')[0][1:].split(',')[0])
                y1 = float(obj['@bounds'].split('][')[0][1:].split(',')[1])
                x2 = float(obj['@bounds'].split('][')[1][:-1].split(',')[0])
                y2 = float(obj['@bounds'].split('][')[1][:-1].split(',')[1])

                print('添加为熟朋友')
                self.adb_tools.adb_click(int(random.uniform(x1, x2)), int(random.uniform(y1, y2)))

                print('确认')
                self.adb_tools.adb_click(int(random.uniform(558, 966)), int(random.uniform(757, 889)))

                print('返回')
                self.adb_tools.adb_click(int(random.uniform(0, 150)), int(random.uniform(72, 216)))

            if obj['@text'] == '添加到通讯录':

                x1 = float(obj['@bounds'].split('][')[0][1:].split(',')[0])
                y1 = float(obj['@bounds'].split('][')[0][1:].split(',')[1])
                x2 = float(obj['@bounds'].split('][')[1][:-1].split(',')[0])
                y2 = float(obj['@bounds'].split('][')[1][:-1].split(',')[1])

                print('添加到通讯录')
                self.adb_tools.adb_click(int(random.uniform(x1, x2)), int(random.uniform(y1, y2)))

                self.adb_tools.adb_dump()

                with open('window_dump.xml', 'r', encoding='utf-8') as rf:
                    window_dump = rf.read()
                    if '验证申请' in window_dump:
                        # 解析布局中的申请内容节点
                        self.analysis(xmltodict.parse(window_dump)['hierarchy']['node'])
                    else:
                        print('返回')
                        self.adb_tools.adb_click(int(random.uniform(26, 98)), int(random.uniform(68, 212)))
                        self.adb_tools.adb_click(int(random.uniform(26, 98)), int(random.uniform(68, 212)))

            if obj.__contains__('@resource-id'):
                if obj['@resource-id'] == 'com.tencent.mm:id/dx6':
                    for item in range(len(obj['@text'])):
                        print('删除字符')
                        self.adb_tools.adb_key(str(67))

                    print('填写申请')
                    self.adb_tools.adb_input('hello')

                    print('发送')
                    self.adb_tools.adb_click(int(random.uniform(855, 1035)), int(random.uniform(100, 190)))

                    print('返回')
                    self.adb_tools.adb_click(int(random.uniform(26, 98)), int(random.uniform(68, 212)))
                    self.adb_tools.adb_click(int(random.uniform(26, 98)), int(random.uniform(68, 212)))

            if obj.__contains__('node'):
                self.analysis(obj['node'])

        elif isinstance(obj, list):
            for item in obj:
                self.analysis(item)

    def add_wechar(self):
        list_phone = ['qq1825203636', 'qq1825203637', '15545825361']

        for item in list_phone:

            phone = item
            print('添加好友：' + phone)

            # 定焦输入框
            print('定焦输入框')
            self.adb_tools.adb_click(int(random.uniform(50, 1035)), int(random.uniform(280, 370)))

            # 填写微信号
            print('填写微信号')
            self.adb_tools.adb_input(phone)

            # 搜索好友
            print('搜索好友')
            self.adb_tools.adb_click(int(random.uniform(55, 190)), int(random.uniform(240, 380)))

            # 获取布局
            self.adb_tools.adb_dump()

            with open('window_dump.xml', 'r', encoding='utf-8') as rf:
                window_dump = rf.read()
                if '添加到通讯录' in window_dump:
                    node_obj = xmltodict.parse(window_dump)['hierarchy']['node']
                    self.analysis(node_obj)
                elif '发消息' in window_dump:
                    print('已经是好友了，返回上一页')
                    self.adb_tools.adb_click(int(random.uniform(26, 98)), int(random.uniform(68, 212)))
                    print('返回上一页')
                    self.adb_tools.adb_click(int(random.uniform(26, 98)), int(random.uniform(68, 212)))
                elif '该用户不存在' in window_dump:
                    print('用户不存在，返回上一页')
                    self.adb_tools.adb_click(int(random.uniform(26, 98)), int(random.uniform(68, 212)))