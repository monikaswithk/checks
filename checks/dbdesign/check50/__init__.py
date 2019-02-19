from check50 import *


class DBDesign(Checks):

    @check()
    def exists(self):
        """main exists"""
        self.require("main.py")
