================
Trash Guy Script
================
**The original Trash Guy animation, written in Python (> ^_^)>🗑**

____________________________

|

.. contents:: **Contents**

Setup Instructions
==================

.. highlights::
    The installation instructions are separated into three sections, the Python Platform, the Operating System and the Text Editor.         Please follow the instructions for each part of the three sections that applies to you in the given order of setup.

Text Editors
------------
Vim
^^^
- Open the vimrc file:

.. code-block:: bash

    vim ~/.vimrc


- Add these lines to the file if they don't exist:

.. code-block::

    set encoding=utf-8  " The encoding displayed.
    set fileencoding=utf-8  " The encoding written to file

- Save and close:

.. code-block::

    :wq

|

Emacs
^^^^^
You can force Emacs to read a file in a specific encoding with ``C-x RET c C-x C-f``. If you opened a file and EMACS determined the encoding incorrectly, you can use ``M-x revert-buffer-with-coding-system``, to reload the file with a named encoding.

You can change the encoding to use for the file when saving using ``C-x C-m f``. You can also force this immediately by using ``C-x C-m c utf-8 RET C-x C-w RET``. You can list all available encodings with ``M-x list-coding-systems``.

You can also mark the entire file with ``C-x h`` and then try ``M-x recode-region``. It will ask you for ``Text was really in`` and ``But was interpreted as``.

|

Notepad++
^^^^^^^^^
You may set the character encoding in Notepad++ as shown in the below image:

.. image:: images/npp.jpg

If doing so still does not display the file correctly, try selecting ``Convert to UTF-8`` and then save the file.

|

Python Platform
---------------
Trash Guy Script was written in ``Python 3.6.3``.
Backwards compatibility has not yet been tested.

To get your current python version type into the terminal:

.. code-block:: bash
    
    python -c "import sys;print(sys.version)"
    
If the command fails to execute, it's possible that no python installation exists.
In that case, please follow `this guide. 
<https://realpython.com/installing-python/>`_ 

Check the output of this command, it should say ``utf-8``.

.. code-block:: bash

    python -c "import sys;print(sys.stdout.encoding)"
    
**If it returns any other value, try to set the default encoding with one of the following platform specific methods:**

Operating Systems
-----------------
Linux
^^^^^
Type this command to see your current locale settings:

.. code-block:: bash

    locale

In the output of the command, check the variable ``LC_ALL=`` to see if it contains ``UTF-8``.
If it does not, try setting it by using the following commands:

.. code-block:: bash

    locale-gen en_US.UTF-8
    export LANG=en_US.UTF-8 LANGUAGE=en_US.en LC_ALL=en_US.UTF-8

Type the ``locale`` command again to confirm that ``LC_ALL=en_US.UTF-8`` has been set.

To confirm that the default encoding has been successfully set, use the code in the snippet `here. <#python-platform>`_

Android
^^^^^^^
    The Android platform default is always UTF-8, however, if the code file does not display correctly, it may have been corrupted. Try     re-downloading it and try again. If that does not solve the problem, refer to the help documentation of the specific                     application/terminal emulator you are using with regards default encoding.

MacOS
^^^^^
Navigate to ``Terminal -> Preferences`` from Terminal’s menu bar.

.. image:: images/macos1.jpg

In the Preferences window select the ``Settings -> Advanced`` tab. 
Then, under the ``Charachter encoding`` drop-down box, select ``Unicode (UTF-8)`` and tick the box ``Set locale environment variables on startup``.

.. image:: images/macos2.jpg

To confirm that the default encoding has been successfully set, use the code in the snippet `here. <#python-platform>`_

Windows
^^^^^^^
Go to ``Start -> Edit environment variables for your account`` or 
``Start -> Edit the system environment variables -> Environment Variables...``
From the ``System variables`` section, click on ``New..``
Under the ``Variable name:`` type in ``PYTHONIOENCODING``
Under the ``Variable value:`` type in ``utf-8``

.. image:: images/windows.jpg

To confirm that the default encoding has been successfully set, use the code in the snippet `here. <#python-platform>`_

|
Usage Examples
==============

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

Setting custom symbols with keyword arguments:

.. code-block:: python

    trash_animation = TrashGuy(user_input, 
                               symbol_trash='V', 
                               symbol_left='<(-.- <)', 
                               symbol_right='(> -.-)>').animate()

|

Like what you see?
==================
⭐️ Star the repository and share with your friends! ⭐️


*Really* like what you see?
---------------------------
*Feel free to buy me some marshmallows* 😁

:Bitcoin: 1CoRm4mKCUPs5XQnFVSVQ4xGMAp29pyYzC

|
⭐️ Supporters and Contributors
==============================
`YouTwitFace`_ | Conceptualized Trash Guy animation for use with Telegram userbots

.. _YouTwitFace: http://github.com/YouTwitFace
