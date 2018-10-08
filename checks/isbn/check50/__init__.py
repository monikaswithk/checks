
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

    @check("exists")
    def ISBN_with_X(self):
        """rejects ISBNs with X as checksum"""
        self.spawn("python isbn.py").stdin("078974984X").reject()

    @check("exists")
    def rejects_ISBNs_with_dashes(self):
        """rejects ISBNs with dashes"""
        self.spawn("python isbn.py").stdin("0-789-75198-4").reject()

    @check("exists")
    def rejects_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("python isbn.py").stdin("").reject()

