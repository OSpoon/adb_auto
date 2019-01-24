#!/usr/bin/env python
# encoding: utf-8

from common.auto_adb import adb_tools
from test_heiyu import heiyu
from test_ltb import ltb
from test_wechar import wechar


if __name__ == '__main__':

    # 初始化adb_tools
    adb_tools = adb_tools()
    # 输出设备信息
    adb_tools.print()

    # 黑域激活命令
    # heiyu(adb_tools).run()

    # 微信添加好友命令
    # wechar(adb_tools).add_wechar()

    # 聊天宝相关
    # ltb(adb_tools).while_send()
    # ltb(adb_tools).read_news()
    # ltb(adb_tools).add_ltb_run()
