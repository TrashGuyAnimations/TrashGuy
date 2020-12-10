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
from typing import Tuple
from .lut import _LUT as LUT
import math
# Defined for 'performance' reasons
sqrt = math.sqrt


class FrameEngine:
    def __init__(self, trash_items: Tuple[str, ...],
                 glyph_can: str,
                 glyph_left: str,
                 glyph_right: str,
                 spacer: str):
        self.trash_items = trash_items
        self.glyph_can = glyph_can
        self.glyph_left = glyph_left
        self.glyph_right = glyph_right
        self.spacer = spacer

        # Length of the input items
        self.t_len = len(trash_items)

        # Calculating frame group sizes and total animation frame count
        # Minimum frame group size, i.e. 6 frames long
        self.min_fg_size = 6

        # Maximum frame group size, i.e. the most of amount of frames needed
        # for throwing away just the last item from beginning to end
        self.max_fg_size_index = self.min_fg_size + (self.t_len * 2)

        # Calculate sum of sizes to get the total animation frame count
        self.total_frame_count = (self.min_fg_size +
                                  self.max_fg_size_index) // 2 * self.t_len

    def convert_linear_index(self, index: int) -> Tuple[int, bool, int]:
        # Map the given index to variables needed for the specific frame
        try:
            # Attempt to look up the index first in the table
            item_index, group_length = LUT[index]
        except IndexError:
            # Alternate method optimized for higher indices
            # Based on submissions by Ceda EI (ceda_ei@webionite.com)
            item_index = int(sqrt(10 + index)) - 3
            group_length = item_index * 2 + 7

        # Median of the frame group size to calculate the apogee of guy
        # where guy hits the item and turns around
        # (similar to Math.ceil of the median float result)
        fg_size_median = group_length // 2

        relative_index = index  # Integers are immutable
        # Faster special case for the first frame group
        if group_length == 7:
            # Calculate the forward direction with index-to-apogee relation
            forward = index < fg_size_median

        # Subsequent frame groups require compensation of previous frame group sums
        else:
            # These equations were generated using AI and algorithms
            all_sum = self.min_fg_size + group_length

            # The sum of frames from all previous frame groups
            previous_frames_sum = all_sum // 2 * item_index

            # The current frame index minus the sum of frames from all previous frame groups
            # to calculate for our relative position within the current frame group
            relative_index = index - previous_frames_sum

            # Calculate the forward direction with relative-index-to-apogee relation
            forward = relative_index < fg_size_median

        # Define where the position should be based on forwards or backwards direction
        if forward:
            position = relative_index + 2
        else:
            position = group_length - relative_index - 1

        # Return the final variables
        return position, forward, item_index

    def get_frame(self, index: int) -> str:
        # input should be sanitized already but for good measure we
        # make sure index is a positive integer over 0 and under max frame len
        san_index = int(index)
        if san_index < 0 or san_index >= self.total_frame_count:
            raise ValueError('index out of range')
        position, forward, item_index = self.convert_linear_index(san_index)

        # Frame Generator
        # Incrementally removes thrown items from the trash pile
        trunc_items = self.trash_items[item_index:]
        # The items which have been removed
        remainder_items = self.trash_items[:item_index]
        # Length of the missing items
        missing_items_len = len(''.join(remainder_items))
        # Calculate the padding based on missing items to keep truncated trash
        # in the same position as things get thrown away
        # (Only applies to points before reaching the trash can with the item)
        padding = [self.spacer] * (missing_items_len + 3)

        # Create a static canvas while each item disappears
        canvas = [self.glyph_can, *padding, *trunc_items]

        # The last item's index that was picked to be trashed
        last_index = len(canvas) - len(trunc_items)

        # Start sequence, forward motion, going right (> ^_^)>
        if forward:
            if position < last_index:
                # Start from second space after the trash can
                canvas[position] = self.glyph_right

                # Snapshot the frames of the animation going right
                return ''.join(canvas)

            # End of forward motion, look left with item
            # Set item position in front of trash guy
            canvas[position - 1] = canvas[last_index]
            # Set position of trash guy where item was
            canvas[position] = self.glyph_left

            # Snapshot frame looking across at trash can
            return ''.join(canvas)

        # Reverse motion, going left <(^_^ <)
        else:
            # Going left with item towards trash can
            if position > 0:
                canvas[position] = self.glyph_left

                # Place item in front while not yet at the trash can
                if canvas[position - 1] != self.glyph_can:
                    canvas[position - 1] = canvas[last_index]

                    # Temporarily remove item from pile while holding it
                    canvas[last_index] = self.spacer

                else:
                    # If trash can reached, replace spacing of missing item
                    if len(self.spacer) == 1:
                        last_item_len = len(canvas[last_index])
                        canvas = (canvas[:last_index] +
                                  [self.spacer] * last_item_len +
                                  canvas[last_index + 1:])
                    else:
                        # Unknown spacer size, use as directed
                        canvas[last_index] = self.spacer

                # Snapshot the frames of the animation going left
                return ''.join(canvas)

            else:  # End of reverse motion, look right for one frame
                canvas[position + 1] = self.glyph_right

                # Temporarily remove item from canvas for last frame also
                if len(self.spacer) == 1:
                    last_item_len = len(canvas[last_index])
                    canvas = (canvas[:last_index] +
                              [self.spacer] * last_item_len +
                              canvas[last_index + 1:])
                else:
                    # Unknown spacer size, use as directed
                    canvas[last_index] = self.spacer

                # Snapshot the frame looking right
                return ''.join(canvas)
