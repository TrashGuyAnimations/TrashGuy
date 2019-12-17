# uncompyle6 version 3.6.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.8.0 (default, Dec 14 2019, 23:51:55) 
# [GCC 7.4.0]
# Embedded file name: .\__main__.py
# Compiled at: 2019-12-17 20:05:57
# Size of source mod 2**32: 183 bytes
from . import eula
import sys
from .trashguy import TrashGuy, Symbols

def main(trash_items):
    print(TrashGuy(*trash_items))


cmd_input = sys.argv[1:]
main(cmd_input)
# okay decompiling __main__.pyc
