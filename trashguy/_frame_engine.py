# uncompyle6 version 3.6.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.8.0 (default, Dec 14 2019, 23:51:55) 
# [GCC 7.4.0]
# Embedded file name: .\_frame_engine.py
# Compiled at: 2019-12-15 22:13:24
# Size of source mod 2**32: 5401 bytes
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
                lower_fg = (*reversed(upper_fg[:-1]), *(1, 0))
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
            raise IndexError('trashguy index out of range')

    @staticmethod
    def get_frame(slc: SliceVars, spr: SpriteVars, index: int) -> str:
        position, forward, item_index = FrameEngine.converter(slc, spr, index)
        trunc_items = spr.trash_items[item_index:]
        missing_items_len = sum(len(x) for x in spr.trash_items[:item_index])
        padding = [spr.spacer] * missing_items_len
        canvas = [
         
          spr.sprite_trash, *[spr.spacer] * 3, *padding, *trunc_items]
        item_truncate_length = -len(trunc_items)
        last_index = len(canvas) - -item_truncate_length
        if item_index < len(spr.trash_items):
            if forward:
                if position < last_index:
                    canvas[position] = spr.sprite_right
                    return FrameEngine.wrap(spr, canvas)
                else:
                    canvas[position - 1] = canvas[last_index]
                    canvas[position] = spr.sprite_left
                    return FrameEngine.wrap(spr, canvas)
            elif position > 0:
                canvas[position] = spr.sprite_left
                if canvas[(position - 1)] != spr.sprite_trash:
                    canvas[position - 1] = canvas[last_index]
                    canvas[last_index] = spr.spacer
                elif len(spr.spacer) == 1:
                    last_item_len = len(canvas[last_index])
                    canvas = canvas[:last_index] + [spr.spacer] * last_item_len + canvas[last_index + 1:]
                else:
                    canvas[last_index] = spr.spacer
                return FrameEngine.wrap(spr, canvas)
            else:
                canvas[position + 1] = spr.sprite_right
                if len(spr.spacer) == 1:
                    last_item_len = len(canvas[last_index])
                    canvas = canvas[:last_index] + [spr.spacer] * last_item_len + canvas[last_index + 1:]
                else:
                    canvas[last_index] = spr.spacer

            return FrameEngine.wrap(spr, canvas)
# okay decompiling _frame_engine.pyc
