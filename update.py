#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("./lib")
import updatesystem

#　单元测试
if __name__ == "__main__":
    args = sys.argv[1:]
    us = updatesystem.UpdateSystem(cli_args=args)
    us.run()

