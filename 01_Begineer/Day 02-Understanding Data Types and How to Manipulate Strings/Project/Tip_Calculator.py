print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))

# Get tip percentage
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip_percent = (bill * tip) / 100
total = bill + tip_percent

# Get number of people and total bill
people = int(input("How many people to split the bill? "))
split = round(total/people, 2)
split = "{:.2f}".format(split)
print(f"Each person should pay: ${split}")
