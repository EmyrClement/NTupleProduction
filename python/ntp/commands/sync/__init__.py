"""
    sync:   Used to synchronise current code base with soolin working area
        Usage:
                sync <NTPROOT on soolin>
"""
from .. import Command as C


class Command(C):

    def __init__(self, path=__file__, doc=__doc__):
        super(Command, self).__init__(path, doc)

    def run(self, args, variables):
        self.__prepare(args, variables)
        self.__text = "NOT IMPLEMENTED"

        return True
