import pandas

with open("file1.txt", 'r') as file:
    lines = file.readlines()
    list_num1 = [int(num.strip('\n')) for num in lines]

with open("file2.txt", 'r') as file2:
    lines = file2.readlines()
    list_num2 = [int(num.strip('\n')) for num in lines]

repeat_numbers = [num for num in list_num1 if num in list_num2]

