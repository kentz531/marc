Chapter 2 - Containers
=======================
This Chapter explains how to store and manipulate data across python

Useful References:
    - cheatsheet for `list.`_
    - cheatsheet for `dictionary.`_

.. _`list.`: https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc_lists.pdf
.. _`dictionary.`: https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc_dictionaries.pdf

Exercise 02
-----------
The Goal for this Exercise is to enhance exercise 01 by allowing the user to input a set of items they want to track

- Input
    .. code-block:: shell

        Budget Calculator . . .
        What's your Name? Marc Philippe
        What is your total Budget for a month? 10000
        What items do you want to track? kiwi,banana
        How many kiwi/s you consume in a month? 20
        How much does kiwi/s cost? 10
        How many banana/s you consume in a month? 30
        How much does banana/s cost? 6

- Output
    .. code-block:: shell

        Dear Marc Philippe,
        Your Projected Budget is described below.
        Total Budget: 10000
        Your kiwi cost: 1000 (10%)
        Your banana cost: 2000 (20%)
        Remaining Budget: 7000 (70%)

Exercise 03
-----------
The Goal for this Exercise is to implement exercise 02 but using dictionary
