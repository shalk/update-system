
import subprocess
import logging

class Task:
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
        try:
            subprocess.check_call(cmd,shell=True)
        except subprocess.CalledProcessError as err:
            print("execute cmd {} fail \n failcode()".format(cmd, 
                err.returncode))

    def content(self):
        """ content of PatchTask
            return string 
        """
        return "father {} child {} path {}".format(self._father,self._children,
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
    a = PatchTask(path="../bugfix/SP1/001/cmd.sh")
    a.run()


