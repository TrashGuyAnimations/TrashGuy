Trash Guy Script
===============
The original Trash Guy animation, written in Python.

Usage Examples
-----------------
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
    
    user_input = message.text.split()  # input from a given message
    
    trash_animation = TrashGuy(user_input).animate()
    for frame in trash_animation:
        asyncio.sleep(0.3)  # external library for sleeping between frames
        message.edit(frame)  # Plays back the animation frame by frame in real time

Like what you see?
--------------
Buy me some marshmallows:

.. epigraph::

1CoRm4mKCUPs5XQnFVSVQ4xGMAp29pyYzC
