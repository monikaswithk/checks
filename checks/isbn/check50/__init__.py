
from check50 import *


class Isbn(Checks):

    @check()
    def exists(self):
        """isbn.py exists"""
        self.require("isbn.py")


    @check("exists")
    def Absolute_Beginners_Guide(self):
        """Beginners Guide (0789751984) valid"""
        self.spawn("python isbn.py").stdin("0789751984").stdout("^YES\n", "YES\n").exit(0)

    @check("exists")
    def Absolute_Beginners_Guide_fake(self):
        """Beginners Guide fake (0789751985) invalid"""
        self.spawn("python isbn.py").stdin("0789751985").stdout("^NO\n", "NO\n").exit(0)

    @check("exists")
    def Programming_in_C(self):
        """Programming in C (0321776410) valid"""
        self.spawn("python isbn.py").stdin("0321776410").stdout("^YES\n", "YES\n").exit(0)

    @check("exists")
    def Hackers_Delight(self):
        """Hackers Delight (0321842685) valid"""
        self.spawn("python isbn.py").stdin("0321842685").stdout("^YES\n", "YES\n").exit(0)

    @check("exists")
    def phone_number(self):
        """Jennys number (6178675309) invalid"""
        self.spawn("python isbn.py").stdin("6178675309").stdout("^NO\n", "NO\n").exit(0)

    @check("exists")
    def memory(self):
        """Mystery Test"""
        self.spawn("python isbn.py").stdin("1632168146").stdout("^YES\n", "YES\n").exit(0)

