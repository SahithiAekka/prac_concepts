#  function parmeters and Ceaser cipher 
# Inputs
# By adding a variable name inside the parentheses when we create (define) a new function, it allows that function to take inputs when called.

# That means we can modify how the function behaves each time by passing in different inputs.

# Creating the function
def myFunction(input):
    print(f"Hey! {input}")
# Using the function
myFunction("Tommy") 

# Inputs are Variables
# When you create a function with inputs, you are defining a variable name that will be given to the data that is passed in.

# The name of the input variable, e.g. name in this code here: def greet(name): is called the parameter.

# The value of the value of the input variable, e.g. Angela when you call the previous greet function: greet("Angela") is called the argument.

def greet():
    print("Hi")
    print("My name is Sahithi ")
    print("I am 25 years old")

greet()

def choco(input):
    print(f"Hey what is your fav chocolate?! Is it???{input} damnn you")

choco("Lindt")

#  input --> parameter , Lindt --> argument
#  the argument is being passed over to the 


# Functions with input
def greet_with_name(name, age):
    print(f"Hello {name}")
    print(f"Are you {age} years old?")

print("********** FUNCTION WITH  MULTIPLE INPUTS - Positional arguments *****************")
greet_with_name("Jack Bauer", 16)
# Positional arguments are important to match with teh position of the parameters
# Keyword arguments 

print("******** FUNCTION WITH  MULTIPLE INPUTS-- Keyword arguments exaple ***************")

greet_with_name(name="Sahithi", age= 25)