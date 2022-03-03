import pandas
import pandas as pd

squirrels = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
black_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])

print(gray_squirrels, black_squirrels, cinnamon_squirrels)


squirrels = pandas.DataFrame({"Fur Color": ["black", "cinnamon", "grey"], "Count": [black_squirrels, cinnamon_squirrels, gray_squirrels]})
squirrels.to_csv('Colors')