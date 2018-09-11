from check50 import *


class Greedy(Checks):

    @check()
    def exists(self):
        """greedy exists"""
        self.require("greedy.py")

    @check("exists")
    def test041(self):
        """input of 0.41 yields output of 4"""
        self.spawn("python greedy.py").stdin("0.41").stdout(coins(4), "4\n").exit(0)

    @check("exists")
    def test001(self):
        """input of 0.01 yields output of 1"""
        self.spawn("python greedy.py").stdin("0.01").stdout(coins(1), "1\n").exit(0)

    @check("exists")
    def test015(self):
        """input of 0.15 yields output of 2"""
        self.spawn("python greedy.py").stdin("0.15").stdout(coins(2), "2\n").exit(0)

    @check("exists")
    def test160(self):
        """input of 1.6 yields output of 7"""
        self.spawn("python greedy.py").stdin("1.6").stdout(coins(7), "7\n").exit(0)

    @check("exists")
    def test230(self):
        """input of 23 yields output of 92"""
        self.spawn("python greedy.py").stdin("23").stdout(coins(92), "92\n").exit(0)

    @check("exists")
    def test420(self):
        """input of 4.2 yields output of 18"""
        self.spawn("python greedy.py").stdin("4.2").stdout(coins(18), "18\n").exit(0)




def coins(num):
    return r"(^|[^\d]){}(?!\d)".format(num)
