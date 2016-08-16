#!/usr/bin/env python
# -*- coding = utf-8 -*-
from updatesystem import task


task = task.PatchTask(path="/root/project/ansible\
        /update-system/02-bugfix/SP1/021/")
print(task)
task.check()
task.run()

