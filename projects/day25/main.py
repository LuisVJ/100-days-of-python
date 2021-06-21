# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")

# # we can convert data to other data types
# data_dict = data.to_dict()

# # Extracting a colum (series) as a list
# temp_list = data["temp"].to_list()
# print(temp_list)

# # Average of the values of a series
# average_temp = data["temp"].mean()
# print(average_temp)

# max_temp = data["temp"].max()
# print(max_temp)

# ## Get data in a row
# print(data[data.day == "Monday"])

# print(data[data.temp == max_temp])

# print("\n\n")

# ## Create a dataframe fro scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# # save the data into a csv file
# data.to_csv("test_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"].unique()
print(color)
data.groupby("Primary Fur Color").size().to_csv("squirrel_count.csv")

