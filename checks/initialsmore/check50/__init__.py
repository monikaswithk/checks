less = __import__("check50").import_from("../initialsless")
from less import *

class InitialsMore(InitialsLess):

    @check("exists")
    def space_between(self):
        """Outputs HJ for hailey       James"""
        self.spawn("python initials.py").stdin("hailey       James", prompt=False).stdout(match("HJ"), "HJ\n").exit(0)

    @check("exists")
    def space_before_after(self):
        """Outputs HJ for     hailey James    """
        self.spawn("python initials.py").stdin("    hailey James    ", prompt=False).stdout(match("HJ"), "HJ\n").exit(0)
