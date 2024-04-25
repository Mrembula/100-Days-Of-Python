# with open("./weather_data.csv", 'r') as file:
#    data = file.readlines()


import csv

with open('./weather_data.csv') as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

import pandas

data = pandas.read_csv("./weather_data.csv")
# print(type(data))
# print(type(data['temp']))
data_dict = data.to_dict()
print(data_dict)
temp_list = data['temp'].to_list()
print(temp_list)

average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

check = data['temp'].mean()
print(data['temp'].max())


# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data['temp'].max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

# Create a dataframe
data_dict = {'students': ['Amy', 'James', 'Angela'],
             'scores': [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
data = squirrel_data['Primary Fur Color'].value_counts()

data.to_csv("count_fur_color")


gray = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'gray'])
black = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'black'])
cinnamon = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'cinnamon'])
print(gray, black, cinnamon)

squirrel_count = {
    'Fur Color': ['Gray', 'Black', 'Cinnamon'],
    'Count': [gray, black, cinnamon]
}

data_1= pandas.DataFrame(squirrel_count)
data_1.to_csv("squirrel_count2")
