Chapter 1 - Hello World
=======================
This Chapter explains the basic syntax and common data types of python

Useful References:
    - `cheatsheet`_ for string formatting.

.. _`cheatsheet`: https://mkaz.blog/code/python-string-format-cookbook/

Exercise 01
---------------------------------------

- Input
    .. code-block:: shell

        Budget Calculator . . .
        What's your Name? Marc Philippe
        What is your total Budget for a month? 10000
        How many apple/s you consume in a month? 20
        How much does apple/s cost? 10
        How many orange/s you consume in a month? 30
        How much does orange/s cost? 6

- Output
    .. code-block:: shell

        Dear Marc Philippe,
        Your Projected Budget is described below.
        Total Budget: 10000
        Your Apple cost: 1000 (10%)
        Your Orange cost: 2000 (20%)
        Remaining Budget: 7000 (70%)

- Code
    .. literalinclude:: exercise01.py
