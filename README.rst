|banner|

|logo| |pyver| |lic| |build| |code| |size| |status| |lastcom| |platforms| |chat| |badgecount|

====================================================
The Original TrashGuy™ Animation!
====================================================
A fun line-based text animation for all your trash disposal needs! Written in Python, this module has full Unicode and emoji support. It can be accessed from the command line directly or used as part of your scripts (i.e., chatbot plugin, loading animations, website widget, etc.)

.. contents:: Contents
   :local:
   :depth: 1


Installation Instructions
=========================

.. code-block:: bash

    pip install trashguy

Or if cloning from repo:

.. code-block:: bash

    git clone https://github.com/TrashGuyAnimations/TrashGuy.git

    python setup.py install

Brief Documentation
===================
Input Arguments
---------------
===================  ================  =============================================================  ======================
**Input Arguments**  **Accepts**       **Description**                                                **Default Value**
-------------------  ----------------  -------------------------------------------------------------  ----------------------
trash_items          Tuple[str, ...]   The item(s) for throwing away 1 character at a time            N/a
glyph_can            String            The emoji/string to be used as the trash can                   Symbols.GLYPH_CAN
glyph_left           String            The string to be used for the left-facing guy                  Symbols.GLYPH_LEFT
glyph_right          String            The string to be used for the right-facing guy                 Symbols.GLYPH_RIGHT
spacer               String            The character/string to be used for spacing the canvas         Symbols.SPACER_DEFAULT
===================  ================  =============================================================  ======================

Symbols Class
-------------
.. highlights::
   Constants from the Symbols class are meant to be used as shortcuts to commonly used strings and symbols. Additionally, they are also used as default values for the input arguments as shown above. However, they are not required for the correct functioning of the animation and can be substituted with custom values of the indicated type. Please note there may be unintended results when using custom values.

==============  ========  =====================  ========================
**Symbols**     **Type**  **Value**              **Rendered As**
--------------  --------  ---------------------  ------------------------
SPACER_DEFAULT  String    "\\u0020"              " "
SPACER_WIDE     String    "\\u2800\\u0020"       "⠀ "
SPACER_EMOJI    String    "\\u2796"              "➖"
GLYPH_CAN       String    "\\U0001F5D1"          "🗑"
GLYPH_LEFT      String    "<(^_^ <)"
GLYPH_RIGHT     String    "(> ^_^)>"
==============  ========  =====================  ========================

Usage Examples
==============

**Command line:**

.. code-block:: bash

    python -m trashguy A B C

**Python module:**

.. code-block:: python

    from trashguy import TrashGuy

    print(TrashGuy('ABC'))
    print(TrashGuy(['📂', '📊', '✉️']))

**Python module as iterator:**

.. code-block:: python

    from trashguy import TrashGuy

    animation = TrashGuy('ABC')

    for frame in animation:
        print(frame)

**Telegram user-bot plugin:**

.. code-block:: python

    from trashguy import TrashGuy, Symbols
    import asyncio

    # {client and handler code omitted}

    user_input = event.message.text  # input from a given message

    animation = TrashGuy(user_input,
                         spacer=Symbols.SPACER_WIDE)  # use wide spacer for better viewing

    for frame in animation:
        asyncio.sleep(0.4)  # external library for sleeping between frames
        wrapped = f'`{frame}`'  # Wrap in backticks for monocode font
        await event.edit(wrapped)  # plays back the animation frame by frame in real time

*Setting custom symbols with keyword arguments and printing as a newline-joined string:*

.. code-block:: python

    from trashguy import TrashGuy, Symbols
    import asyncio

    # {client and handler code omitted}

    user_input = event.message.text  # input from a given message

    animation = TrashGuy(user_input,
                         glyph_can='\u2A06',
                         glyph_left='<(-.- <)',
                         glyph_right='(> -.-)>',
                         spacer=Symbols.SPACER_EMOJI)

    # outputs entire animation with each frame separated by newline with pre-formatted code block markdown
    await event.reply(f'```{animation}```')

*Using HTML formatting:*

.. code-block:: python

    from trashguy import TrashGuy, Symbols
    import asyncio

    # {client and handler code omitted}

    user_input = event.message.text  # input from a given message

    animation = TrashGuy(user_input)

    for frame in animation:
        asyncio.sleep(0.4)
        await event.edit(f'<code>{frame}</code>')

|

Environment Setup
=================

The environment setup steps are separated into three sections, the Text Editor, the Python Platform and the Operating System. Please follow the instructions for each part of the three sections that applies to you in the given order of setup.

.. contents::
   :local:

Text Editors
------------
Vim
^^^
- Open the vimrc file:

.. code-block:: bash

    vim ~/.vimrc


- Add these lines to the file if they don't exist:

.. code-block:: bash

    set encoding=utf-8  " The encoding displayed.
    set fileencoding=utf-8  " The encoding written to file

- Save and close:

.. code-block:: bash

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
If that still fails also, try selecting ``Convert to UTF-8-BOM`` instead, and save the file.

|

Python Platform
---------------
The TrashGuy™ Animation module was written in ``Python 3.7.8``.
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
    The Android platform default is always UTF-8, however, if the code file does not display correctly, it may have been corrupted.
    Try re-downloading it and try again. If that does not solve the problem, refer to the help documentation of the specific application/terminal emulator you are using with regards default encoding.

MacOS
^^^^^
Navigate to ``Terminal -> Preferences`` from Terminal’s menu bar.

.. image:: images/macos1.jpg

In the Preferences window select the ``Settings -> Advanced`` tab.
Then, under the ``Character encoding`` drop-down box, select ``Unicode (UTF-8)`` and tick the box ``Set locale environment variables on startup``.

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

Like what you see?
==================
⭐️ Star the repository and share with your friends! ⭐️

|

⭐️ Supporters and Contributors
===============================
Special thanks to all the folks down on Telegram for their help and support (and patience) - you know who you are!! >_>

|

*TrashGuy™ is an unregistered trademark of Zac (trashguy@zac.cy) protected under the provisions of Common Law and may not be used in the identification of sufficiently similar projects with regard the field of trade where these would cause confusion or damage the trademark of the unregistered trademark owner. All text and images are including the TrashGuy™ (TG) logo are © Zac (trashguy@zac.cy) unless otherwise indicated.*

.. |banner| image:: images/banner.png

.. |logo| image:: https://img.shields.io/badge/%F0%9F%97%91%EF%B8%8F-%3C%28%5E__%5E%20%3C%29-black
    :target: https://travis-ci.com/TrashGuyAnimations/TrashGuy

.. |build| image:: https://travis-ci.com/TrashGuyAnimations/TrashGuy.svg?branch=master
    :target: https://travis-ci.com/TrashGuyAnimations/TrashGuy

.. |lic| image:: https://img.shields.io/pypi/l/trashguy
    :target: https://github.com/TrashGuyAnimations/TrashGuy/blob/master/LICENSE

.. |pyver| image:: https://img.shields.io/pypi/v/trashguy
    :target: https://pypi.org/project/trashguy/

.. |code| image:: https://img.shields.io/codacy/grade/ff6e6515ba5c4ac9bc0cc74c9f3b9957
    :target: https://app.codacy.com/manual/TrashGuyAnimations/TrashGuy

.. |status| image:: https://img.shields.io/pypi/status/trashguy
    :target: https://pypi.org/project/trashguy/

.. |size| image:: https://img.shields.io/github/repo-size/TrashGuyAnimations/TrashGuy
    :target: https://github.com/TrashGuyAnimations/TrashGuy/

.. |lastcom| image:: https://img.shields.io/github/last-commit/TrashGuyAnimations/trashguy
    :target: https://travis-ci.com/TrashGuyAnimations/TrashGuy

.. |platforms| image:: https://img.shields.io/pypi/pyversions/trashguy
    :target: https://github.com/TrashGuyAnimations/TrashGuy/blob/master/README.rst#python-platform

.. |chat| image:: https://img.shields.io/badge/telegram-TrashGuy%20Dev-green
    :target: https://t.me/TrashGuyDev

.. |badgecount| image:: https://img.shields.io/badge/badge%20count-11-blueviolet
    :target: https://shields.io/
