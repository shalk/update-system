
from log import logger as logging
import ConfigParser

config_local_default={
"bugfix": "/home/bugfix",
    }

def safe_get(cf,section,key,default):
    try:
        return cf.get(section,key)
    except ConfigParser.NoOptionError, e:
        logging.debug("NoOptionError" ,exc_info=True)
        return default 
    except:
        logging.warn("exception",exc_info=True)
        return default


def get_config(file="./config.ini",section_name="local"):
    """
    """
    config = dict()
    cf = ConfigParser.ConfigParser()
    try:
        cf.read(file)
        for key in config_local_default:
            config[key] = safe_get(cf,section_name, key, config_local_default[key])
    except IOError,e:
        logging.error("read file failed: {}".format(file),exc_info=True)
    except ConfigParser.NoOptionError, e:
        logging.error("NoOptionError" ,exc_info=True)
    except:
        logging.error("Exception",exc_info=True)
    return config

if __name__ == "__main__":
    print(get_config())

