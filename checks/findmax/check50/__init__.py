

from check50 import *


class findmax(Checks):

    @check()
    def exists(self):
        """findmax.py exists"""
        self.require("findmax.py")

    @check("exists")
    def normalcase(self):
        """normalcase"""
        self.spawn("python findmax.py").stdin("28").stdin("1").stdin("5").stdin("9").stdin("2").stdin("65").stdin("7").stdin("4").stdin("63").stdin("17").stdout("\65\n", "65\n").exit(0)

    @check("exists")
    def allthedame(self):
        """all the same"""
        self.spawn("python findmax.py").stdin("31").stdin("31").stdin("31").stdin("31").stdin("31").stdin("31").stdin("31").stdin("31").stdin("31").stdin("31").stdout("\31\n", "31\n").exit(0)

    @check("exists")
    def negatives(self):
        """allnegatives"""
        self.spawn("python findmax.py").stdin("-31").stdin("-31").stdin("-34").stdin("-31").stdin("-31").stdin("-31").stdin("-31").stdin("-31").stdin("-30").stdin("-32").stdout("\-30\n", "-30\n").exit(0)

    @check("exists")
    def firstismax(self):
        """firstismax"""
        self.spawn("python findmax.py").stdin("29").stdin("2").stdin("2").stdin("1").stdin("-2").stdin("4").stdin("2").stdin("9").stdin("2").stdin("6").stdout("\29\n", "29\n").exit(0)
