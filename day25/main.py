import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_data = data["Primary Fur Color"]

gray_fur = fur_data.value_counts()["Gray"]
cinnamon_fur = fur_data.value_counts()["Cinnamon"]
black_fur = fur_data.value_counts()["Black"]
extracted_data = {
    "fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_fur, cinnamon_fur, black_fur]
}
df = pandas.DataFrame(data=extracted_data)
df.to_csv("squirrel_count.csv")



# data = pandas.read_csv("weather_data.csv")
#
# data_to_dict = data.to_dict()
# print(data_to_dict)
#
# temp_data = data["temp"].to_list()
#
# print(data["temp"].max())
#
# print(data[data.temp == data.temp.max()])
