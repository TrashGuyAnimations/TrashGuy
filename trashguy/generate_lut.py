# ================================================= #
#                Trash Guy Animation                #
#                     (> ^_^)>                      #
#           Made by Zac (trashguy@zac.cy)           #
#               Version 4.1.0+20201210              #
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
def generate_lut(rng: int) -> tuple:
    output = []
    prev = 0
    for i in range(rng):
      x = i * 2 + 7
      for _ in range(prev, prev+x):
         output.append(tuple([i, x]))
      prev += x
    return tuple(output)

def main():
    with open("output.txt", mode="w+") as f:
        f.write(str(generate_lut(30)))

if __name__=="__main__":
    main()