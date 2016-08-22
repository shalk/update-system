
# -*- coding: UTF-8 -*-
import os
from . import configparser 
from . import cli
from .orchestra import Orchestra 

class UpdateSystem(object):
    
    def __init__(self,cli_args=None):
        self.config = self.get_config(cli_args) 
        logging.debug(self.config)
        #self.orchestra = Orchestra(path=orachestra_file)
        #self.conf_path =  os.path.dirname(os.path.abspath(__file__))

    def get_config(self,cli_args):
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
        return config

    def run(self):
        """
        judge what to do
        """
        pass 
    
    def run_orchestra(self):
        pass

    def run_check(self):
        pass

    def run_status(self):
        pass


