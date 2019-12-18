# -*- coding: utf-8 -*-
# =============================================== #
#               Trash Guy Animation               #
#                    (> ^_^)>                     #
#             Made by Zac (t.me/Zacci)            #
#              Version 4.0.0+20191218             #
#        Donate:                                  #
#        1CoRm4mKCUPs5XQnFVSVQ4xGMAp29pyYzC       #
# =============================================== #
# Copyright (C) 2019 Zac (https://t.me/Zacci)     #
# Permission is hereby granted, free of charge,   #
# to any person obtaining a copy of this software #
# and associated documentation files (the         #
# "Software"), to deal in the Software without    #
# restriction, including without limitation the   #
# rights to use, copy, modify, merge, publish,    #
# distribute, sublicense, and/or sell copies of   #
# the Software, and to permit persons to whom     #
# the Software is furnished to do so, subject to  #
# the following conditions: The above copyright   #
# notice and this permission notice shall be      #
# included in all copies or substantial portions  #
# of the Software.                                #
# =============================================== #
#   If you rewrite this software in a different   #
#   programming language or create a derivative   #
#   work, please be kind and include this notice  #
#   and the below credit along with the license!  #
#                                                 #
#    This work is based on the TrashGuy script    #
#     (https://github.com/trash-guy/TrashGuy)     #
#       written by Zac (https://t.me/Zacci).      #
#                                                 #
# =============================================== #
from setuptools import setup, find_packages

setup(
    name='trashguy',
    version=__import__("trashguy").__version__,
    packages=find_packages(),
    license='MIT',
    description = 'The original Trash Guy animation!',
    author = 'Zac',
    author_email = 'thetrashguy@protonmail.ch',
    url = 'https://github.com/trash-guy/TrashGuy',
    keywords = ['Animation', 'ASCII', 'Emoji', 'Fun'],
    include_package_data=False,
    zip_safe=True,
    install_requires=[],
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)