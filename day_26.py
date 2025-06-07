# Day 26 List and Dictonary Comprehensions 


# LIST COMPREHENSIONS 
list_1= [1,2,3,4,5,6,7]
list_2= []

# for n in list_1:
#     add_1 = n + 1
#     list_2.append(add_1)
# print(list_2)

# List comprehension will solve this 
# list_2=[new_item for n in item] where new item is what you want to perform 
list_2 =[n+1 for n in list_1]
print(list_2)

# another example :  making all the letters in a nmae into a list 
name="Sahithi"
letter_list=[letter for letter in name]
print(letter_list) 

# Squaring numbers 
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number*number for number in numbers]


#  DICTONARY COMPREHENSION 
# creating a dict from the values in a list 
# new_dict = {new_key:new_value for item in list}

# creating a new dict from base don the values from the dictonary 
# new_dict ={new_key:new_value for (key,value) in dict.items() if test}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}



weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (temp_c * 9/5) + 32 for day, temp_c in weather_c.items()}

print(weather_f)


# Using loops to iterate over Pandas Data frame using loop 

