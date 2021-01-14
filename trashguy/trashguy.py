# ============================= #
# (> ^_^)>TrashGuy™ Animation   #
#    Version 4.1.0.20210114     #
# ============================= # ========================================= #
# Copyright (C) 2021 Zac (trashguy@zac.cy)                                  #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU Affero General Public License as published  #
# by the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU Affero General Public License for more details.                       #
#                                                                           #
# You should have received a copy of the GNU Affero General Public License  #
# along with this program.  If not, see <https://www.gnu.org/licenses/>.    #
# ========================================================================= #
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
