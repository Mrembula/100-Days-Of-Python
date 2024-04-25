import random
import hangman_art
from hangman_words import word_list


hidden_letters = []
reveal_letters = False
lives = 0
guess_word = ''
# TODO 1 - Randomly choose a word from the word list and assign it to a variable called chosen_word.
random_word = random.choice(word_list)
print(hangman_art.art)

word_length = len(random_word)
for empty in range(0, word_length):
    hidden_letters.append('_')
    guess_word += '_'

print(guess_word)
# TODO 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase

while not reveal_letters:
    guess = input("Guess a letter: ").lower()
    check = word_length - 1
    guessed_word = ''
    if guess in hidden_letters:
        print(f"You already guessed the letter {guess}. Try again")
    else:
        for i in range(0, word_length):
            if guess == random_word[i]:
                hidden_letters[i] = guess

            guessed_word += hidden_letters[i]
        
        if '_' not in hidden_letters:
            print("You win")
            reveal_letters = True
        elif guess not in hidden_letters:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            print(hangman_art.stages[lives])
            lives += 1

            if lives == 5:
                print("You lose")
                reveal_letters = True

        if lives != 5:
            print(guessed_word)
