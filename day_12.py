# Scope 


# local scope 
# Variables (or functions) declared inside functions have local scope (also called function scope). They are only seen by other code within the same block of code.

# e.g.

# def my_function():
#     my_local_var = 2
    
# # This will cause a NameErrorr
# print(my_local_var) 

# global scope 
# Global Scope
# Don't modify the global scope avoid it 
# Variables or functions declared at the top level (unindented) of a code file have global scope. It is accessible anywhere in the code file.

# e.g.

# my_global_var = 3

# def my_function():
#     # This works no problems
    # print(my_global_var)
    

# Block space 





# PRIME NUMBER CHECK 

def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
 
    # Loop through all the numbers between 2 and the number
    for i in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return False
 
    # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
    return True

print(is_prime(3))