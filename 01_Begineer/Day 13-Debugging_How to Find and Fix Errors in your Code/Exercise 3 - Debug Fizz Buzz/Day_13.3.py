for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0: # divisible by 5 or three if one statement is true loop ends here use and operator
        print("FizzBuzz")
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0: # use elif statement if using (if) statement it will check every statement
        print('Buzz')
    else:
        print(number)     # will print square brackets as their in the print statement (remove them[])