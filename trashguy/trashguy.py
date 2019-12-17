# ================================================= #
#                Trash Guy Animation                #
#                     (> ^_^)>                      #
#              Made by Zac (t.me/Zacci)             #
#               Version 4.0.0+20191217              #
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
from typing import Union, Iterator, Tuple
from ._types import SpriteVars, SliceVars
from ._frame_engine import FrameEngine


class Symbols:
    DEFAULT_INPUT = ('\U0001F353', '\U0001F34A', '\U0001F345')
    SPACER_DEFAULT = '\u0020'
    SPACER_WIDE = '\u2800\u0020'
    SPACER_EMOJI = '\u2796'
    WRAPPER_MONOSPACE = '`'
    WRAPPER_BLOCK_MONO = '```'
    SPRITE_CAN = '\U0001F5D1'
    SPRITE_LEFT = '<(^_^ <)'
    SPRITE_RIGHT = '(> ^_^)>'


class TrashGuy:
    def __init__(self, *trash_items: Union[str, Tuple[str, ...]],
                 sprite_can: str = Symbols.SPRITE_CAN,
                 sprite_left: str = Symbols.SPRITE_LEFT,
                 sprite_right: str = Symbols.SPRITE_RIGHT,
                 spacer: str = Symbols.SPACER_DEFAULT,
                 wrapper: str = '',
                 frame_start: int = 0,
                 frames_max: int = None):

        if not trash_items:
            raise TypeError('no trash items given')
        elif not any(trash_items):
            raise TypeError('invalid input "'
                            f'{" ".join([str(i) for i in trash_items])}"')
        elif isinstance(trash_items, str):
            san_trash_items = tuple([str(i) for i in trash_items if i != ' '])
        elif isinstance(trash_items, Tuple):
            temp = []
            for item in trash_items:
                temp += [str(i) for i in item if i != ' ']
            san_trash_items = tuple(temp)
        else:
            raise TypeError('check your input and try again')

        self.sprites = SpriteVars(san_trash_items, sprite_can, sprite_left,
                                  sprite_right, spacer, wrapper)

        self.frame_start = frame_start

        self.index = frame_start - 1

        max_total_frames = self.__len__()
        max_available_frames = max_total_frames - self.frame_start
        if frame_start < 0:
            raise IndexError('frame_start value is too low, expected '
                             'greater or equal to 0, but was given '
                             f'{frame_start} instead')
        elif frame_start >= max_total_frames:
            raise IndexError('frame_start value is too high, expected '
                             f'less or equal to {max_total_frames-1},'
                             f' but was given {frame_start} instead')

        if frames_max is None:
            frames_max = max_available_frames
        elif frames_max > max_available_frames:
            raise IndexError('frames_max value is too high, expected '
                             f'less or equal to {max_available_frames},'
                             f' but was given {frames_max} instead')

        self.slices = SliceVars(frame_start, frames_max)

    def __str__(self):
        return '\n'.join(frame for frame in self)

    def __len__(self) -> int:
        fgv = FrameEngine.frame_group_values(self.sprites)
        total_frame_count = fgv.total_frame_count
        return total_frame_count

    def __getitem__(self, i: Union[int, slice]) -> Union[str, Iterator[str]]:
        if isinstance(i, slice):
            return (self[index] for index in range(*i.indices(len(self))))
        elif isinstance(i, int):
            if i < 0:
                i += len(self)
            if i < 0 or i >= len(self):
                raise IndexError("trashguy index out of range")
            return FrameEngine.get_frame(self.slices, self.sprites, i)
        else:
            raise TypeError(f"trashguy indices must be integers or slices, not {type(i)}")

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        try:
            return FrameEngine.get_frame(self.slices, self.sprites, self.index)
        except IndexError:
            raise StopIteration() from None
