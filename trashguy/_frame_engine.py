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
from ._types import FrameGroupVars, ConversionVars, SpriteVars, SliceVars
from statistics import median


class FrameEngine:
    @staticmethod
    def wrap(sprites: SpriteVars, canvas) -> str:
        wrapper = [sprites.wrapper]
        if sprites.wrapper:
            return ''.join(wrapper + list(canvas) + wrapper)
        else:
            return ''.join(list(canvas))

    @staticmethod
    def frame_group_values(sprites: SpriteVars) -> FrameGroupVars:
        min_fg_size = 6
        max_fg_size_index = min_fg_size + len(sprites.trash_items) * 2
        fg_sizes = range(min_fg_size + 1, max_fg_size_index + 1, 2)
        total_frame_count = sum(fg_sizes)

        return FrameGroupVars(fg_sizes, total_frame_count)

    @staticmethod
    def converter(slc: SliceVars, spr: SpriteVars, index: int) -> ConversionVars:
        fg_sizes, total_frame_count = FrameEngine.frame_group_values(spr)

        temp_frame_index = 0
        if index - slc.frame_start < slc.frames_max:
            for i, fg_size in enumerate(fg_sizes):
                fg = list(range(2, fg_size + 2))
                mid_fg = median(fg)
                upper_fg = fg[:mid_fg - 2]
                lower_fg = *reversed(upper_fg[:-1]), 1, 0

                for pos in upper_fg:
                    if temp_frame_index == index:
                        cv = ConversionVars(pos, True, i)
                        return cv

                    temp_frame_index += 1

                for pos in lower_fg:
                    if temp_frame_index == index:
                        cv = ConversionVars(pos, False, i)
                        return cv

                    temp_frame_index += 1
        else:
            raise IndexError("trashguy index out of range")

    @staticmethod
    def get_frame(slc: SliceVars, spr: SpriteVars, index: int) -> str:
        position, forward, item_index = FrameEngine.converter(slc, spr, index)

        trunc_items = spr.trash_items[item_index:]
        missing_items_len = sum(len(x) for x in spr.trash_items[:item_index])
        padding = [spr.spacer] * missing_items_len

        # Create a dynamic canvas while each item disappears
        canvas = [spr.sprite_trash, *[spr.spacer] * 3, *padding, *trunc_items]
        item_truncate_length = -len(trunc_items)
        last_index = len(canvas) - (-item_truncate_length)

        if item_index < len(spr.trash_items):
            # Start sequence, forward motion, going right
            if forward:
                if position < last_index:
                    # Start from second space after the trash can
                    canvas[position] = spr.sprite_right

                    # Snapshot the frames of the animation going right
                    return FrameEngine.wrap(spr, canvas)

                else:  # End of forward motion, look left with item
                    # Set item position in front of trash guy
                    canvas[position - 1] = canvas[last_index]
                    # Set position of trash guy where item was
                    canvas[position] = spr.sprite_left

                    # Snapshot frame looking across at trash can
                    return FrameEngine.wrap(spr, canvas)

            # Reverse motion, going left
            else:
                # Going left with item towards trash can
                if position > 0:
                    canvas[position] = spr.sprite_left

                    # Place item in front while not yet at the trash can
                    if canvas[position - 1] != spr.sprite_trash:
                        canvas[position - 1] = canvas[last_index]

                        # Temporarily remove item from pile while holding it
                        canvas[last_index] = spr.spacer

                    else:
                        # If trash can reached, replace spacing of missing item
                        if len(spr.spacer) == 1:
                            last_item_len = len(canvas[last_index])
                            canvas = (canvas[:last_index] +
                                      [spr.spacer] * last_item_len +
                                      canvas[last_index + 1:])
                        else:
                            # Unknown spacer size, use as directed
                            canvas[last_index] = spr.spacer

                    # Snapshot the frames of the animation going left
                    return FrameEngine.wrap(spr, canvas)

                else:  # End of reverse motion, look right for one frame
                    canvas[position + 1] = spr.sprite_right

                    # Temporarily remove item from canvas for last frame also
                    if len(spr.spacer) == 1:
                        last_item_len = len(canvas[last_index])
                        canvas = (canvas[:last_index] +
                                  [spr.spacer] * last_item_len +
                                  canvas[last_index + 1:])
                    else:
                        # Unknown spacer size, use as directed
                        canvas[last_index] = spr.spacer

                    # Snapshot the frame looking right
                    return FrameEngine.wrap(spr, canvas)
        # else:
        #    raise IndexError("trashguy index out of range")