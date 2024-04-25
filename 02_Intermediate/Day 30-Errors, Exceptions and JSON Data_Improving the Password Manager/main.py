# FileNotFound
# with open('a_text_file.txt') as file:
#   file.read()

# KeyError
# a_dictionary = {'key1': 'value1', 'key2': 'value2'}
# value = a_dictionary['non_existent_key']

# IndexError
# fruit_list = ['apple', 'banana', 'Pear']
# fruit = fruit_list[3]

# TypeError
# text = 'abc'
# print(text + 5)

# try:
#    file = open("a_file.txt")
#    dictionary = {'key': 'value'}
#    print(dictionary['non_exist'])
# except FileNotFoundError:
#    file = open("a_file.txt", "w")
#    file.write("Hello, World!")
# except KeyError as error_message:
#    print(f"Key doesn't exist: {error_message}")
# else:
#    content = file.read()
#    print(content)
# finally:
#    raise KeyError("This is not a KeyError")


height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Height is greater than 3 meter")

bmi = weight / height ** 2
print(bmi)