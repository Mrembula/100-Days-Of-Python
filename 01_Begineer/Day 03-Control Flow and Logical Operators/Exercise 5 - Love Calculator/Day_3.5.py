print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_names = name1.lower() + name2.lower()

t = combine_names.count('t')
r = combine_names.count('r')
u = combine_names.count('u')
e = combine_names.count('e')

l = combine_names.count('l')
o = combine_names.count('o')
v = combine_names.count('v')
e = combine_names.count('e')

true = t + r + u + e
love = l + o + v + e

combine = int(str(true) + str(love))


if combine < 10 or combine > 90:
    print(f"Your score is {combine}, you go together like coke and mentos.")
elif 40 <= combine <= 50:
    print(f"Your score is {combine}, you are alright together")
else:
    print(f"Your score is {combine}")