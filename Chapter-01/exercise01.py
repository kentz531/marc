# ------------------------------------------
# INPUT
# ------------------------------------------
print("Budget Calculator . . .")

name = input("What's your Name? ")

budget = input("What is your total Budget for a month? " )
count_apple = input("How many apple/s you consume in a month? ")
count_orange = input("How many orange/s you consume in a month? ")


# ------------------------------------------
# PROCESS
# ------------------------------------------
apple_per_piece = 10
orange_per_piece = 6

cost_apple = int(count_apple) * apple_per_piece
cost_orange = int(count_orange) * orange_per_piece
remaining_budget = int(budget) - cost_apple - cost_orange

percent_cost_apple = (cost_apple / int(budget)) * 100
percent_cost_orange = (cost_orange / int(budget)) * 100
percent_remaining_budget = (remaining_budget / int(budget)) * 100

# ------------------------------------------
# OUTPUT
# ------------------------------------------
print("Dear " + name)
print("")
print("Your Projected Budget is described below.")
print("")
print("Total Budget: " + budget)
print("Your Apple cost:  " + str(cost_apple) + " " + str(percent_cost_apple))
print("Your Orange cost:  " + str(cost_orange) + " " + str(percent_cost_orange))
print("Remaining Budget:  " + str(remaining_budget) + " " + str(percent_remaining_budget))
print("")
