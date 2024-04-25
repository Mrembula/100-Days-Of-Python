# The for loop is supposed to iterate start from one to 20 (excluding 20 end at 19)
# The if statement prints a number out if i (variable iteration) is equal to 20
# Debugging -- Nothing's going to display as the iteration exclude 20
# if statement should be i == 19 or range(1, 21)
def my_function():
    for i in range(1, 20):
        if i == 19:
            print("You got it")

# my_function()

# Reproduce the bug
from random import randint
dice_img = ['1', '2', '3', '4', '5', '6']
dice_num = randint(0, 5)
#print(dice_img[dice_num])


# year if statement has to be lesser or equals to 1994
# or change the year to 1995 and greater or equal to 1995 on gen Z
# year = int(input("What's your year of birth?: "))
# if year > 1980 and year <= 1994: # True and False == False
#     print("You are a millenial.")
# elif year > 1994: # False == False
#     print("You are a Gen Z.")


# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at {age}")

# pages = 0
# word_per_page = 0
# pages = int(input("Number of Pages: "))
# word_per_page = int(input("Number of words per page: ")) # double equal
# print(f"{pages} * {word_per_page}")
# total_words = pages * word_per_page
# print(total_words)


#Use a debuggder
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
