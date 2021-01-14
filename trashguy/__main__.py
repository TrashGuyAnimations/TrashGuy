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
import sys
from .trashguy import TrashGuy


def main(trash_items):
    print(TrashGuy(trash_items))


DEFAULT_INPUT = '\U0001F353\U0001F34A\U0001F345'
# 'Temporary' feature to force single character trash items
CMD_LINE = tuple([x for x in sys.argv[1:] if x != ' '])

if CMD_LINE:
    main(CMD_LINE)
else:
    main(DEFAULT_INPUT)
