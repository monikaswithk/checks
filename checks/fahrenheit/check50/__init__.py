from check50 import *


class Fahrenheit(Checks):

    @check()
    def exists(self):
        """fahrenheit.c exists"""
        self.require("fahrenheit.py")


    @check("exists")
    def test37(self):
        """37 degrees Celsius yields 98.6 degrees Fahrenheit"""
        self.spawn("python fahrenheit.py").stdin("37").stdout(number(98.6), "98.6\n").exit(0)

    @check("exists")
    def test0(self):
        """0 degrees Celsius yields 32.0 degrees Fahrenheit"""
        self.spawn("python fahrenheit.py").stdin("0").stdout(number(32.0), "32.0\n").exit(0)

    @check("exists")
    def test100(self):
        """100.00 degrees Celsius yields 212.0 degrees Fahrenheit"""
        self.spawn("python fahrenheit.py").stdin("100.00").stdout(number(212.0), "212.0\n").exit(0)

    @check("exists")
    def testneg40(self):
        """-40 degrees Celsius yields -40.0 degrees Fahrenheit"""
        self.spawn("python fahrenheit.py").stdin("-40").stdout(number(-40.0), "-40.0\n").exit(0)

    @check("exists")
    def test18point5(self):
        """18.5 degrees Celsius yields 65.3 degrees Fahrenheit"""
        self.spawn("python fahrenheit.py").stdin("18.5").stdout(number(65.3), "65.3\n").exit(0)

    @check("exists")
    def testneg123point45678(self):
        """-123.45678 degrees Celsius yields -190.2 degrees Fahrenheit"""
        self.spawn("python fahrenheit.py").stdin("-123.45678").stdout(number(-190.2), "-190.2\n").exit(0)

    @check("exists")
    def test_reject_foo(self):
        """rejects a non-numeric input of "foo" """
        self.spawn("python fahrenheit.py").stdin("foo").reject()

    @check("exists")
    def test_reject_empty_string(self):
        """rejects a non-numeric input of "" """
        self.spawn("python fahrenheit.py").stdin("").reject()



def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
