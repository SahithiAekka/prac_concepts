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
#  **kwarg 

