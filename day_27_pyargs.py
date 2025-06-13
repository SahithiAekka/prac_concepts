# PYTHON ARGUMENTS - Keyword arguments, Positional arguments, Default arguments, Advanced arguments m 
# by creating argumnets that have deafult values =... the arguments are optional because they have a default value 

# *************** POSITIONAL ARGUMNETS ***************************
# How to create a function tht can take unlimited arguments == *args 
#   * - Tells func it can take in any numb arguments 

def add(*args):
    sum=0
    for n in args:
        sum +=n 
    return sum 

print(add(34.5,7,8,7,1,9,0,4,5))

# ****************** KEYWORD ARGUMNETS **************************
#  **kwarg - double astrick -unlimited keyword arguments
# **kwargs allows you to pass a variable number of keyword arguments into a function or method
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")


def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(toast='nah', spam=4, eggs=2)                               
