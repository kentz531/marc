# ------------------------------------------
# INPUT
# ------------------------------------------
print("Budget Calculator . . .")

name = input("What's your Name? ")

budget = int(input("What is your total Budget for a month? " ))
apple_count = int(input("How many apple/s you consume in a month? "))
apple_cost = int(input("How many apple/s you consume in a month? "))
orange_count = int(input("How many orange/s you consume in a month? "))
orange_cost = int(input("How many orange/s you consume in a month? "))


# ------------------------------------------
# PROCESS
# ------------------------------------------
apple_total_cost = int(apple_count) * apple_cost
orange_total_cost = int(orange_count) * orange_cost
percent_cost_apple = (apple_cost / int(budget)) * 100
percent_cost_orange = (orange_cost / int(budget)) * 100

remaining_budget = int(budget) - apple_total_cost - orange_total_cost
percent_remaining_budget = (remaining_budget / int(budget)) * 100

# ------------------------------------------
# OUTPUT
# ------------------------------------------
print(f"Dear {name}")
print("Your Projected Budget is described below.")
print(f"Total Budget: {budget}")
print(f"Your Apple cost:   {apple_total_cost} ({percent_cost_apple:.2f})")
print(f"Your Orange cost:  {orange_total_cost} ({percent_cost_orange:.2f})")
print(f"Remaining Budget:  {remaining_budget} ({percent_remaining_budget:.2f})")
