# ================================================= #
#                Trash Guy Animation                #
#                     (> ^_^)>                      #
#           Made by Zac (trashguy@zac.cy)           #
#               Version 4.1.0.20201210              #
#         Donate:                                   #
#         12Na1AmuGMCQYsxwM7ZLSr1sgfZacZFYxa        #
# ================================================= #
# Copyright (C) 2020 Zac (trashguy@zac.cy)          #
# Permission is hereby granted, free of charge, to  #
# any person obtaining a copy of this software and  #
# associated documentation files (the "Software"),  #
# to deal in the Software without restriction,      #
# including without limitation the rights to use,   #
# copy, modify, merge, publish, distribute,         #
# sublicense, and/or sell copies of the Software,   #
# and to permit persons to whom the Software is     #
# furnished to do so, subject to the following      #
# conditions: The above copyright notice and this   #
# permission notice shall be included in all copies #
# or substantial portions of the Software.          #
# ================================================= #
#
# ================================================= #
#    If you rewrite this software in a different    #
#    programming language or create a derivative    #
#    work, please be kind and include this notice   #
#    and the below credit along with the license:   #
#                                                   #
#    This work is based on the original TrashGuy    #
# animation (https://github.com/trash-guy/TrashGuy) #
#         written by Zac (trashguy@zac.cy).         #
#                                                   #
# ================================================= #
from typing import Union, Generator, Tuple
from ._tgpy_engine import FrameEngine


# TrashGuy Python Library Default Symbols
class Symbols:
    SPACER_DEFAULT = '\u0020'
    SPACER_WIDE = '\u2800\u0020'
    SPACER_EMOJI = '\u2796'

    GLYPH_CAN = '\U0001F5D1'
    GLYPH_LEFT = '<(^_^ <)'
    GLYPH_RIGHT = '(> ^_^)>'


# TrashGuy Python Library Front-End
class TrashGuy:
    def __init__(self, trash_items: Tuple[str, ...],
                 glyph_can: str = Symbols.GLYPH_CAN,
                 glyph_left: str = Symbols.GLYPH_LEFT,
                 glyph_right: str = Symbols.GLYPH_RIGHT,
                 spacer: str = Symbols.SPACER_DEFAULT):

        if not trash_items:
            raise ValueError('no items given')

        self.frame_engine = FrameEngine(trash_items,
                                        glyph_can,
                                        glyph_left,
                                        glyph_right,
                                        spacer)

        self.index = -1

    def __str__(self) -> str:
        return '\n'.join(frame for frame in self)

    def __len__(self) -> int:
        return self.frame_engine.total_frame_count

    def __getitem__(self, i: Union[int, slice]) -> Union[str, Generator]:
        if isinstance(i, slice):
            return (self[index] for index in range(*i.indices(len(self))))
        elif isinstance(i, int):
            if i < 0:
                i += len(self)
            if i < 0 or i >= len(self):
                raise IndexError("index out of range")
            return self.frame_engine.get_frame(i)

        raise TypeError(f"indices must be integers or slices, not {type(i)}")

    def __iter__(self):
        return self

    def __next__(self) -> str:
        self.index += 1
        if self.index < len(self):
            return self.frame_engine.get_frame(self.index)
        else:
            raise StopIteration() from None
