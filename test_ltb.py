#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: test_ltb.py
@time: 2019/1/24 10:45
@desc:
'''
import random

import xmltodict


class ltb():

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

    # 持续发送自定义表情第一排第三个
    def while_send(self):
        while 1:
            self.adb_tools.adb_click(int(random.uniform(838, 1030)), int(random.uniform(1155, 1347)))

    def add_ltb(self):
        self.adb_tools.adb_swipe(30, 749, 30, 417)
        # 获取布局
        self.adb_tools.adb_dump()
        with open('window_dump.xml', 'r', encoding='utf-8') as rf:
            window_dump = rf.read()
            if '添加为熟朋友' in window_dump:
                node_obj = xmltodict.parse(window_dump)['hierarchy']['node']
                self.analysis(node_obj)
            elif '发送消息' in window_dump:
                print('已经是好友了，返回上一页')
                self.adb_tools.adb_click(int(random.uniform(0, 150)), int(random.uniform(72, 216)))

    # 添加聊天宝好友
    def add_ltb_run(self):
        count = 480 / 5

        print(int(count))

        for item in range(int(count)):
            self.adb_tools.adb_click(int(random.uniform(30, 234)), int(random.uniform(417, 649)))

            self.add_ltb()

            self.adb_tools.adb_click(int(random.uniform(234, 438)), int(random.uniform(417, 649)))

            self.add_ltb()

            self.adb_tools.adb_click(int(random.uniform(438, 642)), int(random.uniform(417, 649)))

            self.add_ltb()

            self.adb_tools.adb_click(int(random.uniform(642, 846)), int(random.uniform(417, 649)))

            self.add_ltb()

            self.adb_tools.adb_click(int(random.uniform(846, 1050)), int(random.uniform(417, 649)))

            self.add_ltb()

            self.adb_tools.adb_swipe(30, 649, 30, 417)

    # 阅读聊天宝新闻
    def read_news(self):
        while 1:

            # adb_swipe(24, 375, 24, 1047)
            self.adb_tools.adb_swipe(24, 1047, 24, 175)

            self.adb_tools.adb_click(int(random.uniform(24, 1056)), int(random.uniform(375, 475)))  # 1047

            self.adb_tools.adb_swipe(24, 1047, 24, 175)
            self.adb_tools.adb_swipe(24, 1047, 24, 175)
            self.adb_tools.adb_swipe(24, 1047, 24, 175)
            self.adb_tools.adb_swipe(24, 1047, 24, 175)
            self.adb_tools.adb_swipe(24, 1047, 24, 175)

            self.adb_tools.adb_dump()
            with open('window_dump.xml', 'r', encoding='utf-8') as rf:
                window_dump = rf.read()
                if 'com.bullet.messenger:id/news_share_outside_btn' in window_dump:
                    self.adb_tools.adb_click(int(random.uniform(0, 150)), int(random.uniform(72, 216)))

