import pandas
# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#       H int2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#           Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
invites = []


with open("./Input/Names/invited_names.txt", 'r') as file:
    candidates = file.readlines()
    for name in candidates:
        name = name.strip('\n')
        names.append(name)

with open("./Input/Letters/starting_letter.txt", 'r') as letter:
    line = letter.read()
    for name in names:
        word = line.replace('[name]', name)
        invites.append(word)


for i in range(0, len(names)):
    with open(f"./Output/invitation-to-{names[i]}", 'w') as invitation_letter:
        invitation_letter.write(invites[i])
