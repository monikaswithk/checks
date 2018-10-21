from check50 import *


class InitialsLess(Checks):

    @check()
    def exists(self):
        """initials.py exists."""
        self.require("initials.py")


    @check("exists")
    def uppercase(self):
        """Outputs HLJ for Hailey Lynn James"""
        self.spawn("python initials.py").stdin("Hailey Lynn James", prompt=False).stdout(match("HLJ"), "HLJ\n").exit(0)

    @check("exists")
    def lowercase(self):
        """Outputs HLJ for hailey lynn james"""
        self.spawn("python initials.py").stdin("hailey lynn james", prompt=False).stdout(match("HLJ"), "HLJ\n").exit(0)

    @check("exists")
    def mixed_case(self):
        """Outputs HJ for hailey James"""
        self.spawn("python initials.py").stdin("hailey James", prompt=False).stdout(match("HJ"), "HJ\n").exit(0)

    @check("exists")
    def all_uppercase(self):
        """Outputs B for BRIAN"""
        self.spawn("python initials.py").stdin("BRIAN", prompt=False).stdout(match("B"), "B\n").exit(0)


def match(initials):
    return "^(.*\n)?{}\n".format(initials)