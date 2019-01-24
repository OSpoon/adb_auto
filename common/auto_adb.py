# -*- coding: utf-8 -*-
import os
import random
import subprocess
import platform

import sys

import time


class auto_adb():

    def __init__(self):
        try:
            adb_path = 'adb'
            subprocess.Popen([adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.adb_path = adb_path
        except OSError:
            if platform.system() == 'Windows':
                adb_path = os.path.join(os.getcwd(), 'Tools', 'adb.exe')
                try:
                    subprocess.Popen([adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    self.adb_path = adb_path
                except OSError:
                    pass
            else:
                try:
                    subprocess.Popen([adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except OSError:
                    print('请安装 ADB 及驱动并配置环境变量')
                    exit(1)


    def get_screen(self):
        process = os.popen(self.adb_path + ' shell wm size')
        output = process.read()
        return output


    def run(self, raw_command):
        command = '{} {}'.format(self.adb_path, raw_command)
        process = os.popen(command)
        output = process.read()
        return output


    def test_device(self):
        print('检查设备是否连接...')
        command_list = [self.adb_path, 'devices']
        process = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.communicate()
        if output[0].decode('utf8') == 'List of devices attached\n\n':
            print('未找到设备')
            print('adb 输出:')
            for each in output:
                print(each.decode('utf8'))
            exit(1)
        print('设备已连接')
        print('adb 输出:')
        for each in output:
            print(each.decode('utf8'))


    def test_density(self):
        process = os.popen(self.adb_path + ' shell wm density')
        output = process.read()
        return output

    def test_device_detail(self):
        process = os.popen(self.adb_path + ' shell getprop ro.product.device')
        output = process.read()
        return output


    def test_device_os(self):
        process = os.popen(self.adb_path + ' shell getprop ro.build.version.release')
        output = process.read()
        return output

    def test_adb_path(self):
        return 'ADB PATH : ' + self.adb_path

class adb_tools():

    def __init__(self):
        if sys.version_info.major != 3:
            print('请使用Python3')
            exit(1)
        try:
            from common.auto_adb import auto_adb
        except Exception as ex:
            print(ex)
            print('请将脚本放在项目根目录中运行')
            print('请检查项目根目录中的 common 文件夹是否存在')
            exit(1)
        self._adb = auto_adb()

    def print(self):
        print(self._adb.test_adb_path())
        print(self._adb.test_device_os())
        print(self._adb.test_device_detail())
        print(self._adb.test_density())
        print(self._adb.get_screen())

        self._adb.test_device()

    def adb_run(self, command):
        return self._adb.run(command)

    def adb_click(self, x, y):
        command = 'shell input tap ' + str(x) + ' ' + str(y)
        print('点击：' + command)
        print(self._adb.run(command))
        time.sleep(random.uniform(1, 2))

    def adb_swipe(self, x1, y1, x2, y2):
        command = 'shell input swipe ' + str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2)
        print('滑动：' + command)
        print(self._adb.run(command))
        time.sleep(random.uniform(1, 2))

    def adb_input(self, text):
        command = 'shell input text ' + text
        print('输入：' + command)
        print(self._adb.run(command))
        time.sleep(random.uniform(1, 5))

    def adb_dump(self):
        print('获取布局')
        print(self._adb.run('shell uiautomator dump'))
        print(self._adb.run('pull /sdcard/window_dump.xml'))

    def adb_key(self, key):
        command = 'shell input keyevent ' + key
        print('按键：' + command)
        print(self._adb.run(command))
