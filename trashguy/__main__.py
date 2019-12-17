import sys
from .trashguy import TrashGuy, Symbols

def main(trash_items):
    print(TrashGuy(*trash_items))


cmd_input = sys.argv[1:]
main(cmd_input)
