from check50 import *


class Pennies(Checks):

    @check()
    def exists(self):
        """magic.py exists"""
        self.require("magic.py")
