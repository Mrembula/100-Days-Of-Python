import random

names_string = input("Give me everyone's names, separated by a comma. ")
names = names_string.split(', ')

pay = random.randint(0, len(names) - 1)
print(names[pay] + " is going to buy the meal today.")