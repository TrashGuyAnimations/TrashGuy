# ================================================= #
#                Trash Guy Animation                #
#                     (> ^_^)>                      #
#              Made by Zac (t.me/Zacci)             #
#               Version 4.0.1+20191218              #
#         Donate:                                   #
#         1CoRm4mKCUPs5XQnFVSVQ4xGMAp29pyYzC        #
# ================================================= #
# Copyright (C) 2019 Zac (https://t.me/Zacci)       #
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
# ==========================================-====== #
#    If you rewrite this software in a different    #
#    programming language or create a derivative    #
#    work, please be kind and include this notice   #
#    and the below credit along with the license:   #
#                                                   #
#    This work is based on the original TrashGuy    #
# animation (https://github.com/trash-guy/TrashGuy) #
#       written by Zac (https://t.me/Zacci).        #
#                                                   #
# ================================================= #
from typing import Union, Tuple, List, Generator
from ._types import SpriteVars
from ._frame_engine import FrameEngine


class Symbols:
    DEFAULT_INPUT = ('\U0001F353', '\U0001F34A', '\U0001F345')
    SPACER_DEFAULT = '\u0020'
    SPACER_WIDE = '\u2800\u0020'
    SPACER_EMOJI = '\u2796'
    MARKDOWN_CODE = '`'
    MARKDOWN_PRE = '```'
    HTML_CODE = ('<code>', '</code>')
    HTML_PRE = ('<pre>', '</pre>')
    SPRITE_CAN = '\U0001F5D1'
    SPRITE_LEFT = '<(^_^ <)'
    SPRITE_RIGHT = '(> ^_^)>'


class TrashGuy:
    def __init__(self, *trash_items: str,
                 sprite_can: str = Symbols.SPRITE_CAN,
                 sprite_left: str = Symbols.SPRITE_LEFT,
                 sprite_right: str = Symbols.SPRITE_RIGHT,
                 spacer: str = Symbols.SPACER_DEFAULT,
                 wrapper: Union[str, Tuple[str, str]] = ''):

        if not trash_items:
            raise TypeError('no trash items given')
        elif not any(trash_items):
            raise TypeError('invalid input "'
                            f'{" ".join([str(i) for i in trash_items])}"')

        temp: List[str] = []
        for item in trash_items:
            temp += [str(i) for i in item if i != ' ']
        san_trash_items = tuple(temp)

        sprites = SpriteVars(san_trash_items, sprite_can, sprite_left,
                             sprite_right, spacer, wrapper)

        self.frame_engine = FrameEngine(sprites)

        self.index = -1

    def __str__(self) -> str:
        return '\n'.join(frame for frame in self)

    def __len__(self) -> int:
        return self.frame_engine.frame_group_values().total_frame_count

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
