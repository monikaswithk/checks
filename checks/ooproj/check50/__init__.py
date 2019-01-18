from check50 import *


class OOPProj(Checks):

    @check()
    def exists(self):
        """main exists"""
        self.require("main.py")
