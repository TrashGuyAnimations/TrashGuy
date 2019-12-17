# uncompyle6 version 3.6.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.8.0 (default, Dec 14 2019, 23:51:55) 
# [GCC 7.4.0]
# Embedded file name: .\_types.py
# Compiled at: 2019-12-15 21:47:15
# Size of source mod 2**32: 782 bytes
from typing import NamedTuple, Tuple
FrameGroupVars = NamedTuple('FrameGroupVars', fg_sizes=range,
  total_frame_count=int)
ConversionVars = NamedTuple('ConversionVars', position=int,
  forward=bool,
  item_index=int)
SpriteVars = NamedTuple('SpriteVars', trash_items=(Tuple[(str, ...)]),
  sprite_trash=str,
  sprite_left=str,
  sprite_right=str,
  spacer=str,
  wrapper=str)
SliceVars = NamedTuple('SliceVars', frame_start=int,
  frames_max=int)
# okay decompiling _types.pyc
