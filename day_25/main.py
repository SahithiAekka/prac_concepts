# with open("weather_data.csv") as data_file:
#     data= data_file.readlines()
#     print(data)
    

# import csv #importing csv library

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temp=[]
#     for row in data:
#         print(row[1])
#         temp.append(row[1])
#     print(temp)

# output ---- ['temp', '12', '14', '15', '14', '21', '22', '24']
 
import pandas
data = pandas.read_csv("weather_data.csv")

# print(data["temp"])
#  Output : its beautifully formated
#          day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain
# 2  Wednesday    15      Rain
# 3   Thursday    14    Cloudy
# 4     Friday    21     Sunny
# 5   Saturday    22     Sunny
# 6     Sunday    24     Sunny

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

avg_temp = sum(temp_list)/ len(temp_list)

print(f"The average temp throughout the week is {avg_temp}") 

print(data["temp"].mean())
print(data["temp"].max())

# atrribute and Key have to match inorder to get the data 
print(data["condition"])
print(data.condition)

# Get Data in Columns 
print(data[data.day== "Monday"])

monday= data[data.day== "Monday"]
monday_temp = monday.temp[0]


# Create a data frame from scratch : dataframe is a data structure in python 
data_dict = {
    "students":["Amy","Jake","Terry"],
    "scores": [76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

