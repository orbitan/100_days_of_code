import pandas


def play():
    data = pandas.read_csv("weather_data.csv")
    #  print(data[data.temp == data.temp.max()])
    monday = data[data.day == "Monday"]
    monday_celsius = int(monday.temp)
    print((monday_celsius * 1.8) + 32)


data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
