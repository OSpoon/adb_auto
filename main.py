import random

import xmltodict
from common.auto_adb import adb_tools





def analysis(obj):
    if isinstance(obj, dict):

        if obj['@text'] == '添加为熟朋友':
            x1 = float(obj['@bounds'].split('][')[0][1:].split(',')[0])
            y1 = float(obj['@bounds'].split('][')[0][1:].split(',')[1])
            x2 = float(obj['@bounds'].split('][')[1][:-1].split(',')[0])
            y2 = float(obj['@bounds'].split('][')[1][:-1].split(',')[1])

            print('添加为熟朋友')
            adb_tools.adb_click(int(random.uniform(x1, x2)), int(random.uniform(y1, y2)))

            print('确认')
            adb_tools.adb_click(int(random.uniform(558, 966)), int(random.uniform(757, 889)))

            print('返回')
            adb_tools.adb_click(int(random.uniform(0, 150)), int(random.uniform(72, 216)))


        if obj['@text'] == '添加到通讯录':

            x1 = float(obj['@bounds'].split('][')[0][1:].split(',')[0])
            y1 = float(obj['@bounds'].split('][')[0][1:].split(',')[1])
            x2 = float(obj['@bounds'].split('][')[1][:-1].split(',')[0])
            y2 = float(obj['@bounds'].split('][')[1][:-1].split(',')[1])

            print('添加到通讯录')
            adb_tools.adb_click(int(random.uniform(x1, x2)), int(random.uniform(y1, y2)))

            adb_tools.adb_dump()

            with open('window_dump.xml', 'r', encoding='utf-8') as rf:
                window_dump = rf.read()
                if '验证申请' in window_dump:
                    # 解析布局中的申请内容节点
                    analysis(xmltodict.parse(window_dump)['hierarchy']['node'])
                else:
                    print('返回')
                    adb_tools.adb_click(int(random.uniform(26, 98)), int(random.uniform(68, 212)))
                    adb_tools.adb_click(int(random.uniform(26, 98)), int(random.uniform(68, 212)))

        if obj.__contains__('@resource-id'):
            if obj['@resource-id'] == 'com.tencent.mm:id/dx6':
                for item in range(len(obj['@text'])):
                    print('删除字符')
                    adb_tools.adb_key(str(67))

                print('填写申请')
                adb_tools.adb_input('hello')

                print('发送')
                adb_tools.adb_click(int(random.uniform(855, 1035)), int(random.uniform(100, 190)))

                print('返回')
                adb_tools.adb_click(int(random.uniform(26, 98)), int(random.uniform(68, 212)))
                adb_tools.adb_click(int(random.uniform(26, 98)), int(random.uniform(68, 212)))

        if obj.__contains__('node'):
            analysis(obj['node'])

    elif isinstance(obj, list):
        for item in obj:
            analysis(item)


def add_wechar():
    list_phone = ['qq1825203636', 'qq1825203637', '15545825361']

    for item in list_phone:

        phone = item
        print('添加好友：' + phone)

        # 定焦输入框
        print('定焦输入框')
        adb_tools.adb_click(int(random.uniform(50, 1035)), int(random.uniform(280, 370)))

        # 填写微信号
        print('填写微信号')
        adb_tools.adb_input(phone)

        # 搜索好友
        print('搜索好友')
        adb_tools.adb_click(int(random.uniform(55, 190)), int(random.uniform(240, 380)))

        # 获取布局
        adb_tools.adb_dump()

        with open('window_dump.xml', 'r', encoding='utf-8') as rf:
            window_dump = rf.read()
            if '添加到通讯录' in window_dump:
                node_obj = xmltodict.parse(window_dump)['hierarchy']['node']
                analysis(node_obj)
            elif '发消息' in window_dump:
                print('已经是好友了，返回上一页')
                adb_tools.adb_click(int(random.uniform(26, 98)), int(random.uniform(68, 212)))
                print('返回上一页')
                adb_tools.adb_click(int(random.uniform(26, 98)), int(random.uniform(68, 212)))
            elif '该用户不存在' in window_dump:
                print('用户不存在，返回上一页')
                adb_tools.adb_click(int(random.uniform(26, 98)), int(random.uniform(68, 212)))

def add_ltb():
    adb_tools.adb_swipe(30, 749, 30, 417)
    # 获取布局
    adb_tools.adb_dump()
    with open('window_dump.xml', 'r', encoding='utf-8') as rf:
        window_dump = rf.read()
        if '添加为熟朋友' in window_dump:
            node_obj = xmltodict.parse(window_dump)['hierarchy']['node']
            analysis(node_obj)
        elif '发送消息' in window_dump:
            print('已经是好友了，返回上一页')
            adb_tools.adb_click(int(random.uniform(0, 150)), int(random.uniform(72, 216)))


def add_ltb_main():
    count = 480 / 5

    print(int(count))

    for item in range(int(count)):
        adb_tools.adb_click(int(random.uniform(30, 234)), int(random.uniform(417, 649)))

        add_ltb()

        adb_tools.adb_click(int(random.uniform(234, 438)), int(random.uniform(417, 649)))

        add_ltb()

        adb_tools.adb_click(int(random.uniform(438, 642)), int(random.uniform(417, 649)))

        add_ltb()

        adb_tools.adb_click(int(random.uniform(642, 846)), int(random.uniform(417, 649)))

        add_ltb()

        adb_tools.adb_click(int(random.uniform(846, 1050)), int(random.uniform(417, 649)))

        add_ltb()

        adb_tools.adb_swipe(30, 649, 30, 417)


def news():
    while 1:

        # adb_swipe(24, 375, 24, 1047)
        adb_tools.adb_swipe(24, 1047, 24, 175)

        adb_tools.adb_click(int(random.uniform(24, 1056)), int(random.uniform(375, 475)))# 1047

        adb_tools.adb_swipe(24, 1047, 24, 175)
        adb_tools.adb_swipe(24, 1047, 24, 175)
        adb_tools.adb_swipe(24, 1047, 24, 175)
        adb_tools.adb_swipe(24, 1047, 24, 175)
        adb_tools.adb_swipe(24, 1047, 24, 175)

        adb_tools.adb_dump()
        with open('window_dump.xml', 'r', encoding='utf-8') as rf:
            window_dump = rf.read()
            if 'com.bullet.messenger:id/news_share_outside_btn' in window_dump:
                adb_tools.adb_click(int(random.uniform(0, 150)), int(random.uniform(72, 216)))


def while_send():
    while 1:
        adb_tools.adb_click(int(random.uniform(838, 1030)), int(random.uniform(1155, 1347)))


def activation_hei_yu():
    command = '-d shell sh /data/data/me.piebridge.brevent/brevent.sh'
    print('激活：' + command)
    print(adb_tools.adb_run(command))


if __name__ == '__main__':
    # add_ltb_main()
    # while_send()

    adb_tools = adb_tools()
    adb_tools.print()

    activation_hei_yu()
