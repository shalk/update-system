
# -*- coding: UTF-8 -*-
import os.path
from . import configparser 
from . import cli
from .task import PatchTask
from .check import Checker
from .orchestra import Orchestra 

from .log import logger as logging

class UpdateSystem(object):

    def __init__(self,cli_args=None):
        self.config = self.read_config(cli_args) 
        self.checker = Checker() 
        logging.info(self.config)

    def read_config(self,cli_args):
        """
        配置包含两部分：
        1.命令行
        2.config文件
        先读取 config文件，再读取命令行。 命令行覆盖之前的。
        """
        config_file = configparser.get_config()
        config_cmd  = cli.get_args_config(cli.get_parser(),cli_args) 

        config = dict()
        config = config_file

        for key in config_cmd:
            config[key] = config_cmd[key]
        logging.debug(config)
        return config

    def run(self):
        """
        judge what to do
        """
        if self.config['install']:
            if self.config['install_all']:
                self.run_orchestra()
            elif self.config['install_patch']:
                self.run_task()
            else:
                logging.error("install command fail for unknown task ")
        elif self.config['check']:
            self.run_check()
        elif self.config['status']:
            self.run_status()
        else:
            logging.error("command unknown")

    def run_orchestra(self):
        """
            orchestra file
        """
        orchestra_file_path = self.config.get('orchestra_file_path')
        orchestra_file_name = self.config.get('orchestra_file_name')
        if orchestra_file_name is None :
            logging.error("orchestra_file_name is None in config file")
            return
        if orchestra_file_path is None :
            logging.error("orchestra_file_path is None in config file")
            return

        orchestra_file = os.path.join( orchestra_file_path, orchestra_file_name)
        if not os.path.exists(orchestra_file):
            logging.error("orchestra file {} is not exists!".format(orchestra_file))
            return
        logging.debug("create orchestra by file {}".format(orchestra_file))
        orch = Orchestra(topo_config=orchestra_file)
        task_info_list = orch.topo_order_list()

        for task_path in task_info_list:
            logging.debug("create task {}".format(task_path))
            t = PatchTask(path=task_path)
            t.run()
            if t.run():
                logging.info("run task [{}] success".format(task_path))
            else:
                logging.error("run task [{}] fail".format(task_path))

    def run_task(self):
        for patch_name in self.config['install_patch']:
            task_path = os.path.join(path,patch_name)
            if not os.path.isdir(task_path):
                logging.error("{} is not dir ".format(task_path))
                continue
            logging.debug("create task {}".format(task_path))
            t = PatchTask(path=task_path)
            if t.run():
                logging.info("run task [{}] success".format(patch_name))
            else:
                logging.error("run task [{}] fail".format(patch_name))

    def run_check(self):
        ret = False
        if self.config['check_time'] == "before":
            #print("check_before_update()")
            ret = self.checker.check_before_update()
        elif self.config['check_time'] == "after":
            #print("check_after_update()")
            ret = self.checker.check_after_update()
        else:
            logging.error("check before or after ?")
        return ret

    def run_status(self):
        pass


