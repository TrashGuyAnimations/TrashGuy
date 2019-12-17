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
from typing import NamedTuple, Tuple

FrameGroupVars = NamedTuple('FrameGroupVars',
                            fg_sizes=range,
                            total_frame_count=int)

ConversionVars = NamedTuple('ConversionVars',
                            position=int,
                            forward=bool,
                            item_index=int)

SpriteVars = NamedTuple('SpriteVars',
                        trash_items=Tuple[str, ...],
                        sprite_trash=str,
                        sprite_left=str,
                        sprite_right=str,
                        spacer=str,
                        wrapper=str)

SliceVars = NamedTuple('SliceVars',
                       frame_start=int,
                       frames_max=int)
