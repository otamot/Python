# -*- coding:utf-8 -*-
# 実行すると爆破スイッチが起動して10秒で爆破します。

import commands as cmd
import time

cmd.getstatusoutput("say '爆破スイッチが起動しました'")

for i in range(10):
    time.sleep(1)
    cmd.getstatusoutput("say '"+str(10-i)+"'")

cmd.getstatusoutput("say 'どかああああああん'")
