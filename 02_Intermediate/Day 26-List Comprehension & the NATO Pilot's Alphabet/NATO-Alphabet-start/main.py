import pandas

phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

user_name = input("Enter a word: ").upper()

# TODO 1. Create a dictionary in this format:
phonetic_dic = {phonetic.letter:phonetic.code for index, phonetic in phonetic_alphabet.iterrows()}

# TODO 2.Create a list of the phonetic code words from a word that the user inputs.
phonetic_list = [phonetic_dic[letter] for letter in user_name]
print(phonetic_list)
