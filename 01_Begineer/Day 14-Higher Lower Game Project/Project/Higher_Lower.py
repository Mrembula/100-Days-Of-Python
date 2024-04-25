import art
from game_data import data
from random import choice
from random import randint


# import logo
print(art.logo)


# Create a function that randomly get data
# Get information from a list of dictionary
def get_data():
    random_choice = choice(data)
    return random_choice


data_set = []
# append data to a list and use the index to access the data, assign it to get_data function
for d in range(1, 3):
    data_set.append(get_data())


# Check if data comparison is not the same. If it is then change the second dataset
def same_data(celebrity):
    if data_set[0]['follower_count'] == celebrity['follower_count']:
        celebrity = data[randint(0, len(data)-1)]
    else:
        print()
        return celebrity
    get_random = same_data(celebrity)
    return get_random


data_set[1] = same_data(data_set[1])


# Compare first information A with the second with information B
# Comparing celebrity follower count. The number of follower each celebrity has returning a letter
def compare_followers():
    if data_set[0]['follower_count'] > data_set[1]['follower_count']:
        return 'A'
    else:
        return 'B'


user_score = 0
lost = True

# Play game display which player should decide
# Between A and B if the player decide the right choice game should continue
# Otherwise the game come to an end showing the players score
while lost:
    # print user score
    if user_score != 0:
        print(f"You are right! Current score {user_score}")

    print(f"Compare A: {data_set[0]['name']}, a {data_set[0]['description']}, from {data_set[0]['country']}")
    print(art.vs)
    print(f"Compare B: {data_set[1]['name']}, a {data_set[1]['description']}, from {data_set[1]['country']}")
    answer = compare_followers()

    # Get user input
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # comparing user input answer to the real
    if answer == choice:
        data_set[0] = data_set[1]
        data_set[1] = same_data(data_set[1])
        user_score += 1
    else:
        # clear
        print(art.logo)
        print("Sorry, that's wrong. Final score is ", user_score)
        lost = False
