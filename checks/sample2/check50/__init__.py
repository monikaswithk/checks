from check50 import *

class Sample2(Checks):

    @check()
    def exists(self):

        """sample2.py exists"""
        self.require("sample2.py")



    @check("exists")

    def test_5_output(self):

        """input of nothing yields output of 5"""
        self.spawn("python sample2.py").stdout("5\n", "5\n").exit(0)
