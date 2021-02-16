# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
#
#     print(temp)

import pandas
# data = pandas.read_csv("weather_data.csv")
# monday = data[data.day == 'Monday']
# print(monday.temp)


data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
black_squirrel_count = len(data[data["Primary Fur Color"] == 'Black'])
red_squirrel_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
gray_squirrel_count = len(data[data["Primary Fur Color"] == 'Gray'])

print(black_squirrel_count)
print(red_squirrel_count)
print(gray_squirrel_count)

data_dict = {
    "Fur Color:":["Gray","Cinnamon","Black"],
    "Count:":[gray_squirrel_count,red_squirrel_count,black_squirrel_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")