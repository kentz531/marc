# ---------------------------------------------------
# INPUT
# Ex
# ---------------------------------------------------

your_name = input("What's your name? ")
proj_name = input("What's the name of your project? ")
currency = input("Tell me what currency you want to use? ")
commitment_budget = int(input("How much Commitment have you raised? "))

#
# CAPTURE USER INPUT FOR EXPENDITURE
expenditures = []

print("Please Enter as many expentidure as you want and type 'q' or 'Q' to stop")
while True:
    expenditure = input("How much expenditure have you raised? ")
    if expenditure == 'q' or expenditure == 'Q':
        break

    expenditures.append(int(expenditure))

commitment_utilization = int(input("How Commitment have you utilized? "))

# ---------------------------------------------------
# PROCESS
# ---------------------------------------------------
# Average of expenditure

average_expenditure = sum(expenditures) / len(expenditures)
total_expenditure_percent = 100*(sum(expenditures))/commitment_budget
utilization_percent = 100*(commitment_utilization/commitment_budget)

# ---------------------------------------------------
# OUTPUT
# ---------------------------------------------------


print(" ")
print("---------------------------------------------- ")
print(" ")
print("Dear " + your_name + ",")
print(" ")
print("Your Project " + proj_name + " is described below:")
print(" ")
print("You have Committed Budget for " + str(commitment_budget) + " " + currency)
print(" ")
for expenditure in expenditures:
    print("You allowed: " + str(expenditure) + " " + currency)

print(f"The Average Expenditure is {average_expenditure} {currency}")

print(" ")
print("You have allowed " + str(total_expenditure_percent) + "% to be utilized and you have utilized " + str(utilization_percent)  + "% of the total committed budget.")
