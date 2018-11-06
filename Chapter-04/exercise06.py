# TASK
# Create a function to check if a year is a leap year or not and return True/False
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
