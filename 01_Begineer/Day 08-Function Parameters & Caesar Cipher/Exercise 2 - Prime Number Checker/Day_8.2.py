
def prime_checker(number):
    is_Prime = False
    if number == 2 or number == 3:
        print(f"{number} a is prime number")
    elif number % 2 == 0 or number % 3 == 0:
        print(f"{number} not a prime number")
    else:
        print(f"{number} a prime number")

    """for i in range(2, number):
        if number % i == 0:
            is_Prime = True

    if is_Prime:
        print(f"{number} not a prime number")
    else:
        print(f"{number} a prime number")
    """


n = int(input("Check this number: "))
prime_checker(number=n)