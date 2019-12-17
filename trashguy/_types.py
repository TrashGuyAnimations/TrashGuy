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

