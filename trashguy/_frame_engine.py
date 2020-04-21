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
from collections import deque
from statistics import median
from ._types import FrameGroupVars, ConversionVars, SpriteVars


class FrameEngine:
    def __init__(self, sprites: SpriteVars):
        self.sprites = sprites

    def wrap(self, canvas) -> str:
        canvas_temp = deque(canvas)
        wrap = self.sprites.wrapper
        # Single string provided, prefix and suffix the same
        if isinstance(wrap, str):
            canvas_temp.appendleft(wrap)
            canvas_temp.append(wrap)
        # Two strings provided, prefix and suffix respectively
        elif isinstance(wrap, tuple):
            canvas_temp.appendleft(wrap[0])
            canvas_temp.append(wrap[1])
        return ''.join(canvas_temp)

    def frame_group_values(self) -> FrameGroupVars:
        min_fg_size = 6
        max_fg_size_index = min_fg_size + len(self.sprites.trash_items) * 2
        fg_sizes = range(min_fg_size + 1, max_fg_size_index + 1, 2)
        total_frame_count = sum(fg_sizes)

        return FrameGroupVars(fg_sizes, total_frame_count)

    def converter(self, index: int) -> ConversionVars:
        fg_sizes = self.frame_group_values().fg_sizes

        temp_frame_index = 0
        for i, fg_size in enumerate(fg_sizes):
            f_groups = list(range(2, fg_size + 2))
            mid_fg = int(median(f_groups))
            upper_fg = f_groups[:mid_fg - 2]
            lower_fg = *reversed(upper_fg[:-1]), 1, 0

            for pos in upper_fg:
                if temp_frame_index == index:
                    return ConversionVars(pos, True, i)
                temp_frame_index += 1

            for pos in lower_fg:
                if temp_frame_index == index:
                    return ConversionVars(pos, False, i)
                temp_frame_index += 1
        raise IndexError("index out of range")

    def get_frame(self, index: int) -> str:
        position, forward, item_index = self.converter(index)

        trunc_items = self.sprites.trash_items[item_index:]
        remainder_items = self.sprites.trash_items[:item_index]
        missing_items_len = sum(len(x) for x in remainder_items)
        padding = [self.sprites.spacer] * missing_items_len

        # Create a dynamic canvas while each item disappears
        canvas = [self.sprites.sprite_trash,
                  *[self.sprites.spacer] * 3,
                  *padding, *trunc_items]

        last_index = len(canvas) - len(trunc_items)

        if item_index < len(self.sprites.trash_items):
            # Start sequence, forward motion, going right
            if forward:
                if position < last_index:
                    # Start from second space after the trash can
                    canvas[position] = self.sprites.sprite_right

                    # Snapshot the frames of the animation going right
                    return self.wrap(canvas)

                # End of forward motion, look left with item
                # Set item position in front of trash guy
                canvas[position - 1] = canvas[last_index]
                # Set position of trash guy where item was
                canvas[position] = self.sprites.sprite_left

                # Snapshot frame looking across at trash can
                return self.wrap(canvas)

            # Reverse motion, going left
            else:
                # Going left with item towards trash can
                if position > 0:
                    canvas[position] = self.sprites.sprite_left

                    # Place item in front while not yet at the trash can
                    if canvas[position - 1] != self.sprites.sprite_trash:
                        canvas[position - 1] = canvas[last_index]

                        # Temporarily remove item from pile while holding it
                        canvas[last_index] = self.sprites.spacer

                    else:
                        # If trash can reached, replace spacing of missing item
                        if len(self.sprites.spacer) == 1:
                            last_item_len = len(canvas[last_index])
                            canvas = (canvas[:last_index] +
                                      [self.sprites.spacer] * last_item_len +
                                      canvas[last_index + 1:])
                        else:
                            # Unknown spacer size, use as directed
                            canvas[last_index] = self.sprites.spacer

                    # Snapshot the frames of the animation going left
                    return self.wrap(canvas)

                else:  # End of reverse motion, look right for one frame
                    canvas[position + 1] = self.sprites.sprite_right

                    # Temporarily remove item from canvas for last frame also
                    if len(self.sprites.spacer) == 1:
                        last_item_len = len(canvas[last_index])
                        canvas = (canvas[:last_index] +
                                  [self.sprites.spacer] * last_item_len +
                                  canvas[last_index + 1:])
                    else:
                        # Unknown spacer size, use as directed
                        canvas[last_index] = self.sprites.spacer

                    # Snapshot the frame looking right
                    return self.wrap(canvas)
        raise IndexError("index out of range")
