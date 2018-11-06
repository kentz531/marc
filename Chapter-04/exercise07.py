# This function came from exercise06
def is_leap(year):
    if not 1900 <= year <= 10 ** 5:
        raise ValueError

    leap = False

    # Write your logic here
    if year % 400 == 0 and year % 100 == 0 and year % 4 == 0:
        leap = True
    elif not year % 400 == 0 and not year % 100 == 0 and year % 4 == 0:
        leap = True

    return leap


# TASK
# is to sum all the days in a given start and end year
# considering leap years

start_year = int(input("Start Year: "))
end_year = int(input("End Year: "))

years = range(start_year, end_year + 1)

# STRATEGY 1
leap_count = 0
for year in years:
    if is_leap(year):
        leap_count += 1

total_days_in_leap = leap_count * 366
total_days_no_leap = (len(years) - leap_count) * 365

total_days_0 = total_days_in_leap + total_days_no_leap

# STRATEGY 2
total_days_1 = 0
for year in years:
    if is_leap(year):
        total_days_1 += 366
    else:
        total_days_1 += 365

# STRATEGY 3
total_days_2 = 0
for year in years:
    total_days_2 += 366 if is_leap(year) else 365

# STRATEGY 4
total_days_3 = sum([366 if is_leap(i) else 365 for i in years])

print(total_days_0)
print(total_days_1)
print(total_days_2)
print(total_days_3)
