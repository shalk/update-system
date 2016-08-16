
# -*- coding: UTF-8 -*-
import os
import sys
import subprocess
import ssl
import urllib2
import traceback
import shlex
reload(sys)
sys.setdefaultencoding('utf-8')

from log import logger as logging

# monkey patch
ssl._create_default_https_context = ssl._create_unverified_context
installed_patch_list = []


def get_cm_ip():
    return u"10.0.33.145"

def check_cmd_match_result(cmd, expect_output, success_str=None,
        failed_str=None):
    """
    """
    cmd_list = shlex.split(cmd)
    try:
        output = subprocess.check_output(cmd_list,stderr=subprocess.STDOUT)
        output = output.strip()
        logging.debug(output)
        if output == expect_output:
            return True
        else:
            logging.debug("expect:({})".format(expect_output))
            logging.debug("actual:({})".format(output))
            return False
    except subprocess.CalledProcessError,e :
        logging.debug(e.output)
        logging.debug(cmd)
        logging.debug("Exception",exc_info=True)
        return False
    except:
        logging.debug(cmd)
        logging.debug("Exception", exc_info=True)
        return False

def check_cm_visit():
    """
    检查cm可以访问
    """
    url="https://{ip}/".format(ip=get_cm_ip())
    #url="http://10.0.33.148:8000/navi/"
    req = urllib2.Request(url)
    s = urllib2.urlopen(req)
    if s.getcode() == 200:
        #logging.info(s.info())
        logging.info("connect cm  success(code:{})".format(s.code))
        return True
    else:
        logging.error("can not connect cm (code:{})".format(s.code))
        return False

def check_patch_md5(path="./"):
    """
    检查patch完整性
    """
    logging.info("patch path:{}".format(os.getcwd()))
    if not os.path.exists(path):
        logging.error("{} is not exists! ".format(path))
        return False
    try:
        os.chdir(path)
    except:
        logging.error("chdir directory {} fail".format(path))
        return False

    try:
        output = subprocess.check_output(["/usr/bin/md5sum", "-c",
            "./md5"],stderr=subprocess.STDOUT)
        logging.info("output:{}".format(output))
        return True
        #retcode = 0
        #if retcode != 0:
        #    logging.error("{}md5 check failed".format(path))
        #    return False
        #else:
        #    return True
    except subprocess.CalledProcessError,e :
       # for line in e.output.split("\n"):
       #     logging.error(line) 

        logging.debug(e.output)
        logging.debug("Exception",exc_info=True)
        logging.error("{}md5 check failed".format(path))
        return False
    except :
        #logging.exception()
        logging.debug("Exception",exc_info=True)
        logging.error("{}md5 check failed".format(path))
        return False

def check_self_version():
    """
    """
    return True

def check_service_version():
    """
    """
    cmd_dict = {
            "rabbitmq":
            {"cmd": "rpm -q rabbitmq-server" , 
            "result":"rabbitmq-server-3.3.5-16.el7.noarch",},
            "redis":
            {"cmd": "rpm -q redis",
            "result":"redis-2.8.19-2.el7.x86_64",},
            "mariadb":
            {"cmd":"rpm -q mariadb-server" ,
            "result":"mariadb-server-5.5.44-2.el7.centos.x86_64",},
            "tomcat":
            {"cmd":"ls -d /usr/local/apache-tomcat-8.0.32/",
            "result":"/usr/local/apache-tomcat-8.0.32/" },
            }
    for name in cmd_dict:
        ret = check_cmd_match_result(cmd_dict[name]["cmd"],
        cmd_dict[name]["result"])
        if ret :
            logging.info( "service {}  version is right  ".format(name))
        else:
            logging.error( "service {} version is not match".format(name)) 

def check_service_status():
    """
    """
    ret = True
    service_name=["rabbitmq-server","redis","tomcat","mariadb"]
    for name in service_name:
        cmd = "service {} status".format(name)
        try:
            cmd_list = shlex.split(cmd)
            output = subprocess.check_output(cmd_list,stderr=subprocess.STDOUT)
            logging.info("{} status is OK".format(name))
            logging.debug(output)
            retcode = 0
        except subprocess.CalledProcessError, e:
            #logging.error(e.output) 
            #logging.exception("Exception")
            logging.debug(cmd)
            logging.debug("Exception",exc_info=True)
            logging.error("service {} status check failed ".format(name))
            ret = False
        except :
            logging.debug(cmd)
            logging.debug("Exception",exc_info=True)
            logging.error("service {} may be not exists".format(name))
            ret = False
    return ret


def check_cm_version(expect_version):
    version_file="/usr/local/apache-tomcat-8.0.32/webapps/ROOT/WEB-INF/classes/version.properties"
    try:
        with open(version_file,"r") as f:
            line=f.read()
            version=line.strip.split("=")[1]
            logging.info(version)
            if version == expect_version:
                return True
            else:
                logging.error("cm version {} not match.(expect {})"\
                        .format(version, expect_version))
                return False
    except:
        logging.debug("Exception",exc_info=True)
        logging.error("open version file {} failed ".format(version_file)) 
        return False



def check_cm_patch_status():
    """
    """
    installed_patch_list = []
    if not os.path.exists("/usr/local/cm"):
        return installed_patch_list
    try:
        os.chdir("/usr/local/cm")
        output = subprocess.check_output("ls")
        installed_patch_list = output.strip().split("\n")
    except:
        logging.debug("",exc_info=True)
    return installed_patch_list


def check_cm_file_status():
    return True

def check_cm_task_running():
    url = u"xxx"
    req = urllib2.Request(url)
    s = urllib2.urlopen(req)
    info = s.read()
    logging.info("running task:{}".format(info))
    if info != "None":
        return False
    else:
        return True

def check_cm_online_people():
    url = "xxx"
    req = urllib2.Request(url)
    s = urllib2.urlopen(req)
    info = s.read()
    logging.info("online people:{}".format(info))
    if info != "0":
        return False
    else:
        return True

def check_system_space():
    s = os.statvfs("/")
    size = s.f_bavail * s.f_frsize
    logging.debug(" avail block {}".format(size))
    if size < 1024 * 1024:
        logging.error("remain size less than 1G")
        return False
    else:
        logging.info("system space is enough")
        return True

def check_before_update():
    env_ok = False
    expect_version = "2.0.36053.20160811R"
    env_ok = check_cm_visit() 
    env_ok = check_patch_md5() or env_ok
    #env_ok = check_self_version()  or env_ok 
    env_ok = check_service_version() or   env_ok 
    env_ok = check_service_status()  or env_ok 
    env_ok = check_cm_version(expect_version) or  env_ok 
    installed_patch_list = check_cm_patch_status()  or env_ok 
    #env_ok = check_cm_file_status() or env_ok 
    #env_ok = check_cm_task_running()  or env_ok 
    #env_ok = check_cm_online_people() or  env_ok 
    env_ok = check_system_space() or  env_ok 
    if env_ok:
        logging.info("enviroment: OK")
    else:
        logging.error("enviroment: Fail")

def check_after_update():
    env_ok = check_service_status() 
    env_ok = check_cm_visit() or ret
    if env_ok:
        logging.info("enviroment: OK")
    else:
        logging.error("enviroment: Fail")

if __name__ == "__main__":
    check_before_update()
