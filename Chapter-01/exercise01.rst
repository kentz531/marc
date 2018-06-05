# Input:
# ------------------------------------------

    Budget Calculator . . .

    What's your Name? Marc Philippe

    What is your total Budget for a month? 10000

    How many apple/s you consume in a month? 20

    How many orange/s you consume in a month? 30


# Output:
# ------------------------------------------

    Dear Marc Philippe,

    Your Projected Budget is described below.

    Total Budget: 10000

    Your Apple cost: 1000 (10%)

    Your Orange cost: 2000 (20%)

    Remaining Budget: 7000 (70%)


# Pseudo Programming:
# ------------------------------------------
    Dear <name>,

    Your Projected Budget is described below.

    Total Budget: <budget>

    Your Apple cost: <cost_apple> (<percent_cost_apple>)

    Your Orange cost: <cost_orange> (<percent_cost_orange>)

    Remaining Budget: <remaining_budget> (<percent_remaining_budget>)

    apple_per_piece = 10

    orange_per_piece = 6

    cost_apple = count_apple * apple_per_piece

    cost_orange = count_orange * orange_per_piece

    remaining_budget = budget - cost_apple - cost_orange

    percent_cost_apple = cost_apple / budget

    percent_cost_orange = cost_orange / budget

    percent_remaining_budget = remaining_budget / budget
