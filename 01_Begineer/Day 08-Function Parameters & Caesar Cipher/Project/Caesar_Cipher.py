import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # Added alphabets (caesar)
print(art.logo)

while True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    def caesar_cipher(plain_text, shift_amount, shift_direction):
        new_text = ""
        new_position = 0
        for letter in plain_text:
            if letter.isalpha():
                position = alphabet.index(letter)
                if direction == 'encode':
                    new_position = position + shift_amount % 26
                elif direction == 'decode':
                    new_position = position - shift_amount % 26
                new_text += alphabet[new_position]
            else:
                new_text += letter

        print(f"The {shift_direction}d text is {new_text}")


    caesar_cipher(plain_text=text, shift_amount=shift, shift_direction=direction)
    again = input("Type 'yes' if you want to go again, or 'no' to exit:\n").lower()
    if again == 'yes':
        continue
    else:
        break


#   Angela's solution
'''def caesar(plain_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction} text is {end_text}")


caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)'''