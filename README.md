### adb_auto

使用Python来执行adb命令

##### 使用方法

1. 初始化adb_tools

   ```
   adb_tools = adb_tools()
   ```

2. 输出连接信息和设备信息

   ```
   adb_tools.print()
   ```

3. 执行命令

   常用:

   ```
   adb_tools.adb_click(int(random.uniform(838, 1030)), int(random.uniform(1155, 1347)))
   ```

   ```
   adb_tools.adb_swipe(24, 1047, 24, 175)
   ```

   ```
   adb_tools.adb_input('hello')
   ```

   ```
   adb_tools.adb_dump()
   ```

   ```
   adb_tools.adb_key(str(67))
   ```

   其他:

   ```
   command = '-d shell sh /data/data/me.piebridge.brevent/brevent.sh'
   print('激活：' + command)
   print(adb_tools.adb_run(command))
   ```

##### 注释

- auto_adb.py中的auto_adb类来自开源项目wechat_jump_game
- Tools目录来自开源项目wechat_jump_game
- 添加adb_tools类添加adb_click,adb_swipe,adb_input,adb_dump,adb_key及adb_run
- 修改默认adb执行出现OSError时Tools下adb.exe的引用