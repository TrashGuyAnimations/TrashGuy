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
from typing import Tuple
from math import sqrt


class FrameEngine:
    def __init__(self, trash_items: Tuple[str, ...],
                 glyph_can: str,
                 glyph_left: str,
                 glyph_right: str,
                 spacer: str):
        self.trash_items = list(trash_items)
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
        item_index = 0
        group_length = 7
        # Attempt to look up the index first in a loop for indices under 160
        if index < 160:
            previous_index = 7
            # Modified on original code provided by Painor (github.com/painor)
            while True:
                if previous_index > index:
                    break
                item_index += 1
                # Calculate the length of the frame group
                group_length = item_index * 2 + 7
                # The new value of the animation length
                previous_index += group_length
        # Alternate method optimized for indices of 160 or higher
        else:
            # Alternate method suited for higher indices
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

        # Subsequent groups require compensation of previous frame group sums
        else:
            # These equations were written with the help of AI and algorithms
            all_sum = self.min_fg_size + group_length

            # The sum of frames from all previous frame groups
            previous_frames_sum = all_sum // 2 * item_index

            # Current frame index minus sum of frames from all
            # previous frame groups to calculate for relative position
            # within the current frame group
            relative_index = index - previous_frames_sum

            # Calculate the forward direction with relative-index-to-apogee
            forward = relative_index < fg_size_median

        # Define the position based on forwards or backwards direction
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
        all_items = self.trash_items

        # Incrementally removes thrown items from the trash pile
        trunc_items = all_items[item_index:]

        # The items which have been removed
        remainder_items = all_items[:item_index]

        # Length of the missing items (not flattened)
        missing_items_len = len(''.join(remainder_items))

        # Length of the current item
        current_len = len(current_item)

        # Calculate the padding based on missing items to keep truncated trash
        # in the same position as things get thrown away
        space = self.spacer

        # (Only applies to points before reaching the trash can with the item)
        padding = [space] * (missing_items_len + 3)

        # Create a static canvas while each item disappears
        canvas = [self.glyph_can] + padding + trunc_items

        # The last item's index that was picked to be trashed
        last_index = len(canvas) - len(trunc_items)

        # Start sequence, forward motion, going right (> ^_^)>
        if forward:
            if position < last_index:
                # Start from second space after the trash can
                canvas[position] = self.glyph_right
                canvas[position-1] = space

                # Snapshot the frames of the animation going right
                return ''.join(canvas)

            # End of forward motion, look left with item
            # Set item position in front of guy
            canvas[position - 1] = current_item
            # Set position of guy where item was
            canvas[position] = self.glyph_left
            canvas[position - 2] = space

            # Snapshot frame looking across at trash can
            return ''.join(canvas)

        # Reverse motion, going left <(^_^ <)
        else:
            if position > 0:  # Going left with item towards trash can
                canvas[position] = self.glyph_left
                # Place item in front while not yet at the trash can
                if canvas[position - 1] != self.glyph_can:
                    # Set item position in front of guy
                    canvas[position - 1] = current_item
                    # Temporarily remove item from pile while holding it
                    canvas[last_index] = space

                    # Snapshot the frame looking left
                    return ''.join(canvas)

            else:  # End of reverse motion, look right for one frame
                canvas[position + 1] = self.glyph_right
            # If trash can reached, replace spacing of missing item
            # or temporarily remove item from canvas for last frame
            if len(space) == 1:
                canvas = (canvas[:last_index] +
                          [space] +
                          canvas[last_index + 1:])
            else:
                # Other spacer size, use as directed
                canvas[last_index] = space

            # Snapshot the frame looking right
            return ''.join(canvas)
