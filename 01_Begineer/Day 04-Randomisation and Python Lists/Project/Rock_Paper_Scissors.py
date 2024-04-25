import random
user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors "))
if user_choice > 2 or user_choice < 0:
    print("Invalid input.")
else:
    computer_choice = random.randint(0,2)
    print(computer_choice)
    game = ['Rock', 'Paper', 'Scissors']

    user = game[user_choice]
    computer = game[computer_choice]

rock = ''' _______ 
    	 ---' ____) 
    	     (_____) 
    	      (_____) 
    	      (____) 
        ---.__(___) \n'''

paper = '''   _______ 
    	    ---' ____)____ 
    		        ______) 
    		        _______) 
    		       _______) 
    	   ---.__________) \n'''

scissors = ''' _______ 
    	      ---' ____)____ 
    		          ______) 
    		       __________) 
    		       (____) 
    	     ---.__(___) \n'''


if user == "Rock":
    if computer == "Paper":
        print(f"{paper}computer chose:\nPaper")
        print(f"{rock}You lose")

    elif computer == "Scissors":
        print(f"{scissors}computer chose:\nScissors")
        print(f"{rock}You win")
    else:
        print(computer)
        print(f"{rock}Computer chose:\nRock")
        print(f"{rock}It's A tie")

elif user == "Paper":
    if computer == "Paper":
        print(f"{paper}computer chose:\nPaper")
        # print ASCII
        print(f"{paper}It's a tie")
    elif computer == "Scissors":
        print(f"{scissors}computer chose:\nScissors")
        # print ASCII
        print(f"{paper}You lose")
    else:
        print(f"{rock}Computer chose:\nRock")
        print(f"{paper}You win")

elif user == "Scissors":
    if computer == "Paper":
        print(f"{paper}computer chose:\nPaper")
        # print ASCII
        print(f"{scissors}You win")
    elif computer == "Scissors":
        print(f"{scissors}computer chose:\nScissors")
        # print(user)
        print(f"{scissors}It's a tie")
    else:
        print(f"{rock}Computer chose:\nRock")
        print(f"{scissors}You lose")
