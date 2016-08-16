#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from updatesystem import task
from updatesystem import orchestra 
from updatesystem.cli import parser
# TODO
#　单元测试
#  日志控制
#  命令行接口 

def command_line():
    args = parser.parse_args()
    print(args)

command_line()

orch = orchestra.Orchestra("./02-bugfix/SP1/patch.list")

#orch.print_topology()

#for task_path in orch.task_list:
#    ptask = task.PatchTask(path=task_path)
#    #print(ptask)
#    ptask.check()
#    ptask.run()
#



