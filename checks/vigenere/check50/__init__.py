from check50 import *


class Vigenere(Checks):

    @check()
    def exists(self):
        """vigenere.c exists."""
        self.require("vigenere.py")

    @check("exists")
    def aa(self):
        """encrypts "a" as "a" using "a" as keyword"""
        self.spawn("python vigenere.py a").stdin("a").stdout("ciphertext:\s*a\n", "ciphertext: a\n").exit(0)

    @check("exists")
    def bazbarfoo_caqgon(self):
        """encrypts "barfoo" as "caqgon" using "baz" as keyword"""
        self.spawn("python vigenere.py baz").stdin("barfoo").stdout("ciphertext:\s*caqgon\n", "ciphertext: caqgon\n").exit(0)

    @check("exists")
    def mixedBaZBARFOO(self):
        """encrypts "BaRFoo" as "CaQGon" using "BaZ" as keyword"""
        self.spawn("python vigenere.py BaZ").stdin("BaRFoo").stdout("ciphertext:\s*CaQGon\n", "ciphertext: CaQGon\n").exit(0)

    @check("exists")
    def allcapsBAZBARFOO(self):
        """encrypts "BARFOO" as "CAQGON" using "BAZ" as keyword"""
        self.spawn("python vigenere.py BAZ").stdin("BARFOO").stdout("ciphertext:\s*CAQGON\n", "ciphertext: CAQGON\n").exit(0)

    @check("exists")
    def bazworld(self):
        """encrypts "world!$?" as "xoqmd!$?" using "baz" as keyword"""
        self.spawn("python vigenere.py baz").stdin("world!$?").stdout("ciphertext:\s*xoqmd!\$\?\n", "ciphertext: xoqmd!$?\n").exit(0)

    @check("exists")
    def withspaces(self):
        """encrypts "hello, world!" as "iekmo, vprke!" using "baz" as keyword"""
        self.spawn("python vigenere.py baz").stdin("hello, world!").stdout("ciphertext:\s*iekmo, vprke!\n", "ciphertext: iekmo, vprke!\n").exit(0)

    @check("exists")
    def noarg(self):
        """handles lack of argv[1]"""
        self.spawn("python vigenere.py").exit(1)

    @check("exists")
    def toomanyargs(self):
        """handles argc > 2"""
        self.spawn("python vigenere.py 1 2 3").exit(1)

    @check("exists")
    def reject(self):
        """rejects "Hax0r2" as keyword"""
        self.spawn("python vigenere.py Hax0r2").exit(1)