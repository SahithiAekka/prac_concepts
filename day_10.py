# Function with outputs 
# building a calculator app 

# Regular functions 
# Function with inputs my_func("name",price)

# Function with outputs 

def my_func():
    result = 3*3
    return result

output= my_func()
print(output)


def format_name(f_name,l_name):
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()

    print(f"Hello {formated_f_name} {formated_l_name}")

format_name("sahIthi", "AekkA")

#  using return 
def format_name(f_name,l_name):
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()

    return f"Hello {formated_f_name} {formated_l_name}"

formated_string= format_name("sahIthi", "AekkA")
print(formated_string)

 

# output of function 1 to become input of function 2 

def func1(text):
    return text + text

def func2(text):
    return text.title()

output=func2(func1("hello"))

print(output)


#  MULTIPLE RETURNS 
# Return tells the computer when the function ends and you can have multiple of returns 
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name?"), input("What is your last name?")))



# Leap year 
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# DOCSTRINGS 
# creating documentation as we're coding . It goes as the first line after delceration of our function . in between """ three quation marks """
# 

