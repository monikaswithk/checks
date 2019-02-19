from check50 import *


class SQLProj(Checks):

    @check()
    def exists(self):
        """main exists"""
        self.require("main.py")
