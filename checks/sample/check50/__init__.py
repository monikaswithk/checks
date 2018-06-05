from check50 import *

class Sample(Checks):

    @check()
    def exists(self):

        """sample.py exists"""
        self.require("sample.py")



    @check("exists")

    def test_5_output(self):

        """input of nothing yields output of 5"""

        self.spawn("./python sample.py").stdout("5\n", "5\n").exit(0)