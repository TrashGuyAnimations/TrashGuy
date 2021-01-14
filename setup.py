# -*- coding: utf-8 -*-
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
from setuptools import setup, find_packages

setup(
    name='trashguy',
    version=__import__("trashguy").__version__,
    packages=find_packages(),
    license='AGPLv3+',
    description='The Original TrashGuy™ Animation!',
    long_description='A fun line-based text animation for all your trash disposal needs! Written in Python, this module has full Unicode support. It can be accessed from the command line directly or used as part of your scripts (i.e., chatbot plugin, loading animations, website widget, etc.)',
    author='Zac',
    author_email='trashguy@zac.cy',
    url='https://github.com/TrashGuyAnimations/TrashGuy',
    keywords=['Animation', 'ASCII', 'Emoji', 'Fun'],
    include_package_data=False,
    zip_safe=True,
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
