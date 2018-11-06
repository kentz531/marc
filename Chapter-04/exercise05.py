# input_check('Budget')
# input_check('Count')
# input_check('Cost')
def input_check(name):
    while True:
        input_variable = int(input(name))
        if input_variable > 0:
            break

    return input_variable


# ------------------------------------------
# INPUT
# ------------------------------------------
print("Budget Calculator . . .")

name = input("What's your Name? ")

budget = input_check("What is your total Budget for a month? ")

# input: apple,orange,kiwi,banana
# [apple, orange, kiwi, banana]
items = input("What items do you want to track? ")
items = items.split(',')

items_list = []
# [apple, orange, kiwi, banana]
for i in items:
    item_count = input_check(f"How many {i}/s you consume in a month? ")
    item_cost = input_check(f"{i} Cost: ")

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
