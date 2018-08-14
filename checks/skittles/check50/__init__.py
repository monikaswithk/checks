from check50 import *


class Skittles(Checks):

    @check()
    def exists(self):
        """skittles exists"""
        self.require("skittles.py")

