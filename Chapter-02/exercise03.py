# ------------------------------------------
# INPUT
# ------------------------------------------
print("Budget Calculator . . .")

name = input("What's your Name? ")

while True:
    budget = int(input("What is your total Budget for a month? "))
    if 0 < budget <= 5000:
        break

# input: apple,orange,kiwi,banana
# [apple, orange, kiwi, banana]
items = input("What items do you want to track? ")
items = items.split(',')

items_list = []
# [apple, orange, kiwi, banana]
for i in items:
    while True:
        item_count = int(input(f"How many {i}/s you consume in a month? "))
        if item_count > 0:
            break
    while True:
        item_cost = int(input(f"{i} Cost: "))
        if item_cost > 0:
            break

    item = {
        'name': i,
        'cost': item_cost,
        'count': item_count
    }

    items_list.append(item)

# ------------------------------------------
# PROCESS
# ------------------------------------------
for item in items_list:
    item['total_cost'] = item['cost'] * item['count']
    item['percent_cost'] = (item['total_cost'] / budget) * 100

remaining_budget = budget - sum([d['total_cost'] for d in items_list])
remaining_percent_budget = 100 - sum([d['percent_cost'] for d in items_list])

# ------------------------------------------
# OUTPUT
# ------------------------------------------
print(f"Dear {name},")
print(f"Your Projected Budget is described below.")
print(f"Total Budget:       {budget}")

for item in items_list:
    print(f"Your {item['name']} cost:    {item['total_cost']} ({item['percent_cost']:.2f}%)")

print(f"Remaining Budget:   {remaining_budget} ({remaining_percent_budget:.2f}%)")
