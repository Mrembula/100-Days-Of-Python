import random
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

computer = random.randint(1, 100)
attempts = 0

if level == 'easy':
    attempts = 10
elif level == 'hard':
    attempts = 5

while attempts != 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == computer:
        print("You got it! The answer was " + str(computer))
        break
    elif guess < computer:
        print("Too low")
    else:
        print("Too high")
    attempts -= 1
    print(attempts)
    print("Guess again")

if attempts == 0:
    print(f"Game Over you lose guess is {computer}")
