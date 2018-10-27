# ------------------------------------------
# INPUT
# ------------------------------------------
print("Budget Calculator . . .")
name = input("What's your Name? ")
budget = int(input("What is your total Budget for a month? "))

# input: apple,orange,kiwi,banana
# [apple, orange, kiwi, banana]
items = input("What items do you want to track? ")
items = items.split(',')

items_count = []
items_cost = []

# [apple, orange, kiwi, banana]
for i in items:
    item_count = int(input(f"How many {i}/s you consume in a month? "))
    item_cost = int(input(f"{i} Cost: "))

    items_count.append(item_count)
    items_cost.append(item_cost)

# ------------------------------------------
# PROCESS
# ------------------------------------------
items_total_cost = []
items_percent_cost = []

for index, element in enumerate(items):
    item_total_cost = items_cost[index] * items_count[index]
    items_total_cost.append(item_total_cost)

    item_percent_cost = (items_total_cost[index] / budget) * 100
    items_percent_cost.append(item_percent_cost)

remaining_budget = budget - sum(items_cost)
remaining_percent_budget = 100 - sum(items_percent_cost)

# ------------------------------------------
# OUTPUT
# ------------------------------------------
print(f"Dear {name},")
print(f"Your Projected Budget is described below.")
print(f"Total Budget:       {budget}")

for index, element in enumerate(items):
    item = items[index]
    item_total_cost = items_total_cost[index]
    item_percent_cost = items_percent_cost[index]
    print(f"Your {item} cost:    {item_total_cost} ({item_percent_cost:.2f}%)")

print(f"Remaining Budget:   {remaining_budget} ({remaining_percent_budget:.2f}%)")
