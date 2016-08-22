#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
from updatesystem import task
from updatesystem import orchestra 
from updatesystem.cli import parser,get_args_config
# TODO
#　单元测试
#  日志控制
#  命令行接口 

import updatesystem


if __name__ == "__main__":
    args = sys.argv[1:]
    us = updatesystem.UpdateSystem(cli_args=args)
    us.run()

#def command_line():
#    args = parser.parse_args()
#    config = get_args_config(parser, sys.argv[1:])
#    #print(args)
#
#command_line()
#
#orch = orchestra.Orchestra("./02-bugfix/SP1/patch.list")

#orch.print_topology()

#for task_path in orch.task_list:
#    ptask = task.PatchTask(path=task_path)
#    #print(ptask)
#    ptask.check()
#    ptask.run()
#



