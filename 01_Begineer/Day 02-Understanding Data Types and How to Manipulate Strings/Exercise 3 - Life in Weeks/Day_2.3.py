age = input("What is your current age? ")

remaining = 90 - int(age)

days = remaining * 365
weeks = remaining * 52
months = remaining * 12

print(f"You have {days} days, {weeks} weeks, and {months} left.")
