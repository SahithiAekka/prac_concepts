# Randomization 
# random module 
# Pseudo random number genetarors - Mersen Twister 

import random 

print(random.randint(1,100)) 
# Generated a random number btw 1 and 100 inclusing  both 1 and 100 
random_num=random.randint(1,100)
print(random_num)
# my module creating my own module


# random floating point numbers 
random_float=random.random() # always includes zero but not 1 
# returns a ranmdom floating number btw 0.0 and 1.0, 0.0 <= X >= 1.0 0 is inclusive but 1 is not inclusive 
print(random_float)


#Lists 
# list is a data dtucture , data structire is a way of storing and organizing data 
# set of square brackets with data types you can also have mixed ones 
states_of_america=["Illionis", "Michigan","California","Arizona", "Nevada"]
print(states_of_america)


# Bill random 
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
card_selected=random.choice(friends)
print(card_selected)

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st Option
print(random.choice(friends))

#indexing 
#index error, when you're working with list with large ammount of data you can have out of range error 
dirty_dozen=["strawberries","spinach","nectrane","peaches","blueberries","tomatoes"]