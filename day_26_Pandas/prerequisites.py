#
# data = []
# with open("./weather_data.csv") as weather:
#     entries = weather.readlines()
#     for entry in entries:
#         entry = entry.split()
#         data.append(entry)
#
# print(data)
#
# weather.close()

import csv
data_list = []
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)