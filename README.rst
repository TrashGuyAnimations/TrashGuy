================
Trash Guy Script
================
**The original Trash Guy animation, written in Python (> ^_^)>🗑**


.. contents:: **Contents**

Installation Instructions
=========================

.. highlights::
    The installation instructions are separated into three sections, the Python Platform, the Operating System and the Text Editor.         Please follow the instructions for each part of the three sections that applies to you in the given order of setup.

Text Editors
------------
Nano
^^^^

    
Vim
^^^


Emacs
^^^^^


Notepad++
^^^^^^^^^

Python Platform
---------------

Operating Systems
-----------------
Linux
^^^^^

Android
^^^^^^^

MacOS
^^^^^

Windows
^^^^^^^

Usage Example
=============

Using from the command line (space delimited arguments):

.. code-block:: bash

    python trashguy.py A B C

Using as a python module (arguments split into a list):

.. code-block:: python

    from trashguy import TrashGuy
    
    user_input = 'A B C'.split()  # input must be a list
    
    trash_animation = TrashGuy(user_input).animate()
    print(*trash_animation, sep='\n')  # result is also a list
    
Using as a plugin to a telegram userbot:

.. code-block:: python

    from trashguy import TrashGuy
    import asyncio
    
    # {client and handler code omitted}
    
    user_input = event.message.text.split()  # input from a given message
    
    # specifying keyword telegram properly formats the frames for viewing on telegram
    trash_animation = TrashGuy(user_input, telegram=True).animate()
    for frame in trash_animation:
        asyncio.sleep(0.3)  # external library for sleeping between frames
        await event.edit(frame)  # plays back the animation frame by frame in real time


Like what you see?
==================
⭐️ Star the repository and share with your friends! ⭐️


*Really* like what you see?
---------------------------
*Feel free to buy me some marshmallows* 😁

:Bitcoin: 1CoRm4mKCUPs5XQnFVSVQ4xGMAp29pyYzC


⭐️ Supporters and Contributors
==============================
`YouTwitFace`_ | Conceptualized Trash Guy animation for use with Telegram userbots

.. _YouTwitFace: http://github.com/YouTwitFace
