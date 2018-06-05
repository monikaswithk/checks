import re

from check50 import *

class Test(Checks):

    @check()
    def exists(self):
        """Test.java exists."""
        self.require("Test.java")

    @check("exists")
    def compiles(self):
        """Test.java compiles."""
        self.spawn("javac Test.java").exit(0)

    @check("compiles")
    def prints_hello(self):
        """prints "hello\\n" """
        expected = "[Hh]ello?\n"
        actual = self.spawn("java Test").stdout()
        if not re.match(expected, actual):
            err = Error(Mismatch("hello\n", actual))
            if re.match(expected[:-1], actual):
                err.helpers = "Did you forget a newline (\"\\n\") at the end of your System.out.println string?"
            raise err