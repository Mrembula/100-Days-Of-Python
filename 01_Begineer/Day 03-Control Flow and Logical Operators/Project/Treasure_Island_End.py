print("Welcome to Treasure Island Entry")
print("Your mission is to find the Island's Treasure\n")
print("You're in a two way route:\n""1.Left - A Tunnel which is underground\n""2.Right- Full of trees which "
      "leads to the jungle\n")
choice = input("Select 'Left' or 'Right'? \nNB: Please only write your answers with words within the single bracket "
               "notation: ").lower()

if choice == "left":
    print("You come across a sign that allows to to only pick one object a 'gun' or 'torch'")
    choice = input("Pick one object? ").lower()

    if choice == "gun":
        print("The tunnel keeps getting darker as you go deeper as you tried turning back, you fell in to a hole to "
              "your doom")
    if choice == "torch":
        print("The tunnel kept getting darker as you go, but good for you, you got a torch and see a hole")
        print("This hole can be jumped but if you put work into jumping it, but on your left these a curtain covering "
              "something you can't actually see")
        choice = input("So what's your choice 'curtains' or 'jump'? ").lower()
        if choice == "curtains" or choice == "curtain":
            print("You come across a ladder to help cross the to help you cross the hole.")
            print("Let's get going as you pass the step ladder you lost your torch in the pitch black"
                  "Not getting it back it's over for the the torch")
            choice = input("What's your move 'forward' or 'back'? ").lower()
            if choice == "back":
                print("The dark isn't safe for no one. You were killed by beat lurking in the shadows")
            elif choice == "forward":
                print("As the tunnel become light you are on your way out of the tunnel")
                print("As you make it out of the tunel. Congratulations! you found the treasure")
        else:
            print("Jump! You are almost there! Ah damn you never made the hole was too wide.")

if choice == "right":
    print("Walking by you come across a an old person that allow you to choose between a weapon and a vehicle to help "
          "pass the jungle")
    choice = input("So what's your pick 'vehicle' or 'weapon'? ").lower()
    if choice == "weapon":
        print("As you make it across the jungle, with nothing but your weapon you come across a person who needs help "
              "getting around the jungle he make eye contact and calls you out in a different language")
        choice = input("So what's your pick 'help' or 'pass'. ").lower()
        if choice == "help":
            print("Okay, so as you help the this strange person you just met in the jungle. In the middle of nowhere."
                  "He calls out his people and they take all your belongings, take all you weapons leaving defenceless")
            choice = input("So what's your option, do you keep 'walking' or 'end' the hunt ").lower()
            if choice == ("walking" or "walk") or "end":
                print("As you walking you come across a a wild animal. You tried running but couldn't out run it"
                      ". Better luck next time")
        elif choice == "pass":
            print("Okay, as you pass the strange person in the jungle. Some ,moments later you meet up with a wild "
                  "animal and it rushes towards you with no good intentions")
            choice = input("Remembering that you've got some tools on you, you remain unfazed, "
                           "so what is it going to be. remain and 'fight' the wild animal or 'flee' from the animal ").lower()
            if choice == "fight":
                print("As you hustle and tussle with the animal, you finally win the fight as the wild animal flees"
                      "So the road is nothing but straight ahead and as you walk by in the wilderness jungle you "
                      "finally see the treasure. Congratulations! You managed to win the game ")
            elif choice == "flee":
                print("Great! You tried running you couldn't out run the wild animal as it devours you. "
                      "Sorry but better luck next time.")
    if choice == "vehicle":
        print("Let go get that treasure. As drive on the road. The road get too narrow and small for you to keep "
              "driving\nSo do you keep 'driving' or 'walk'.")
        choice = input("What is your choice? ").lower()
        if choice == "drive" or choice == "driving":
            print("The road keeps getting smaller and as you force your way down hill. The car falls of a cliff to "
                  "your doom. Sorry but you never made it out alive as the car exploded during the fall")
        elif choice == "walk":
            print("As you walking you come across a a wild animal. You tried running but could out run it"
                  "Should have chose the weapon")

