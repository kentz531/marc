Chapter 2 - Containers
=======================
This Chapter explains how to control the flow of your codes, by using conditional statements

Useful References:
    - reference for `conditional statements.`_

.. _`conditional statements.`: https://realpython.com/python-conditional-statements/

Exercise 04
-----------
The Goal for this Exercise is to enhance exercise 03 adding constrains, disallowing input value less than or equal to 0

- Input
    .. code-block:: shell

        Budget Calculator . . .
        What's your Name? Marc Philippe
        What is your total Budget for a month? -10000
        What is your total Budget for a month? 10000
        What items do you want to track? kiwi,banana
        How many kiwi/s you consume in a month? -20
        How many kiwi/s you consume in a month? 20
        How much does kiwi/s cost? 10
        How many banana/s you consume in a month? -30
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
