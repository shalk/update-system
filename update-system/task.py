
import subprocess
import shlex
from log import logger as logging

class Task(object):
    def __init__(self,*argv,**kwargv):
        pass


class PatchTask(Task):
    """

    """
    def __init__(self, path):
        self.path = path
        self._father = "father"
        self._children = "child"

    def check(self):
        pass

    def run(self):
        cmd = "bash {}".format(self.path)
        #cmd_list = shlex.split(cmd)
        logging.debug("excute cmd ({})".format(cmd))
        try:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
            logging.debug(output)
        except subprocess.CalledProcessError , e:
            logging.debug("Exception",exc_info=True)
            logging.error("execute {} failed".format(cmd))
        except:
            logging.debug("Exception",exc_info=True)
            logging.error("execute {} failed".format(cmd))

    def content(self):
        """ content of PatchTask
            return string 
        """
        return "father: {}\n child :{}\n path {}\n".format(self._father,self._children,
                self.path)

    def revert(self):
        pass

    @property
    def father(self):
        return self._father

    @father.setter
    def father(self,father):
        self._father = father

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self,children):
        self._children=  children



if __name__ == "__main__":
    a = PatchTask(path="../02-bugfix/SP1/021/test.sh")
    a.father = "base"
    a.child = "039"
    a.run()
    print(a.content())


