from check50 import *


class Caesar(Checks):

    @check()
    def exists(self):
        """caesar.c exists."""
        self.require("caesar.py")


    @check("exists")
    def encrypts_a_as_b(self):
        """encrypts "a" as "b" using 1 as key"""
        self.spawn("python caesar.py 1").stdin("a").stdout("ciphertext:\s*b\n", "ciphertext: b\n").exit(0)

    @check("exists")
    def encrypts_barfoo_as_yxocll(self):
        """encrypts "barfoo" as "yxocll" using 23 as key"""
        self.spawn("python caesar.py 23").stdin("barfoo").stdout("ciphertext:\s*yxocll\n", "ciphertext: yxocll\n").exit(0)

    @check("exists")
    def encrypts_BARFOO_as_EDUIRR(self):
        """encrypts "BARFOO" as "EDUIRR" using 3 as key"""
        self.spawn("python caesar.py 3").stdin("BARFOO").stdout("ciphertext:\s*EDUIRR\n", "ciphertext: EDUIRR\n").exit(0)

    @check("exists")
    def encrypts_BaRFoo_FeVJss(self):
        """encrypts "BaRFoo" as "FeVJss" using 4 as key"""
        self.spawn("python caesar.py 4").stdin("BaRFoo").stdout("ciphertext:\s*FeVJss\n", "ciphertext: FeVJss\n").exit(0)

    @check("exists")
    def encrypts_barfoo_as_onesbb(self):
        """encrypts "barfoo" as "onesbb" using 65 as key"""
        self.spawn("python caesar.py 65").stdin("barfoo").stdout("ciphertext:\s*onesbb\n", "ciphertext: onesbb\n").exit(0)

    @check("exists")
    def handles_no_argv(self):
        """handles lack of argv[1]"""
        self.spawn("python caesar.py").exit(1)