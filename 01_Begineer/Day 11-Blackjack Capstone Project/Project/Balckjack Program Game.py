import art
import random
from replit import clear


print(art.logo)
# ################## Blackjack Project ###########################

# Difficulty Normal: Use Hints below to complete the project.
# Difficulty Hard: only Hints 1, 2, 3to complete the project
# Difficulty Extra Hard: Only user Hints 1 & 2 to complete the project
# Difficulty Expert: Only Hint 1 to complete the project


# ############## Our Blackjack House Rules ######################

# #The deck is unlimited in size.
# #There are no jokers.
# #The Jack/ Queen/King all count as 10.
# #The Ace can count as 11 or 1.
# #Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# #The cards in the list have equal probability of being drawn.
# #Cards are not removed from the deck as they are drawn.

# ########################### Hints ##############################

# Hints 1: Go to this website and try the blackjack game:
#   https =://games.washingtonpost.com/ games/blackjack/
# Then try out the completed Blackjack project here:
#   https://blackjack-final.appbrewery.repl.run


# Hint 2: Read this breakdown of the program requirements:
#   https://listmoz.com/view/6h34JpvJBFVRlZfvxF
# Then try to create your own flowchart

# Hint 4: Create a deal_card() function that the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
def deal_card():
    return random.choice(cards)


# Hints 6: Create a function called calculate_score() that takes a list of cards as input
# and returns the score.
# Look up the sum() function to help you do this

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the
# user's score is over 21, then the game ends
def calculate_score(card_list):
    total_score = sum(card_list)
    for card in card_list:
        # Hint 7: inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
        # and return 0 instead of the actual score. 0 will represent a blackjack in our game.
        if total_score == 21:
            return 21
        elif total_score > 21 and 11 in card_list:
            # Hint 8: Inside calculate_score() check for 11 (ace) if the score is already over 21,
            # remove the 11 and replace it with 1.You might need to look up append and remove().
            for find_card in card_list:
                if find_card == 11:
                    card_list.remove(find_card)
                    card_list.append(1)
                    total_score -= 10

    return total_score


# Hint 13: Create a function called compare() and pass in the user_score() and computer_score().
# If the computer and user both have the same score, then it;s a draw. If the computer has a blackjack
# (0) then the user loses. If the user has a blackjack (0) the user wins
# If thw user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses
# None of the above, then the payer with the biggest score wins
def compare(computer, user):
    print(f"Your final hand{user_cards}, final score: {user_score}")
    print(f"Computer's final hand{computer_cards}, final score: {computer_cards}")
    if computer == user:
        print("It's a draw")
    elif computer == 0:
        print("Lose, opponent has Blackjack")
    elif user == 0:
        print("Win with a Blackjack")
    elif user > computer and user > 21:
        print("You went over. You Lose")
    elif computer > user and computer > 21:
        print("Opponent went over. You Win")
    elif user > computer:
        print("You win")
    elif user < computer:
        print("You lose")


play_again = False
while not play_again:
    user_score = 0
    computer_score = 0
    draw = 'yes'

    # Hint 5: Deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    for i in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while True:  # Hint 11: The score will needs to be rechecked with every new card drawn and checks in Hint
        # 9 need to be repeated until game ends
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards:{user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or user_score == 21:
            compare(computer_score, user_score)
            break
        elif computer_score == 0 or computer_score == 21:
            compare(computer_score, user_score)
            break
        elif user_score > 21 or computer_score > 21:
            compare(computer_score, user_score)
            break
            # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes,
            # then use the deal_card() function to add another card to user_card List. If no, then the game has ended
        if user_score < 21 and draw == 'yes' or draw == 'y':
            draw = input("Would you like to draw another card?: ").lower()
            if draw == "yes" or draw == "y":
                user_cards.append(deal_card())

        #  Hint 12: Once the user is done and no longer wants more cards, it's time to let the computer play
        # The computer should keep drawing cards as long as it has a score less than 17
        if computer_score < 21:
            if computer_score < 17:
                computer_cards.append(deal_card())
            elif computer_score > 17 and draw == 'no' or draw == 'n':
                compare(computer_score, user_score)
                break

    # Hints 14: Ask the user if they want to restart the game. If they answer yes, clear the console
    # and start a new game of blackjack and show the logo from art.py
    choice = input("Would you like to play again: ")
    if choice == "no" or choice == "n":
        play_again = True
    elif choice == "yes" or choice == "y":
        clear()
    else:
        break
