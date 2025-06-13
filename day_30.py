# Try: Something that might cause an exception 
# Except: Do this if there was an exception
# Else: Do this if there were no exception 
# Finally: Do this no matter what happens 
# you can have multiple expetions : you can get hold of the exceptions

try:
    file =open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["sdfsdf"])
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("Something")
except KeyError as error_message:
    print(f"the key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
# finally:
#   raise TypeError("This is an error that I made up")

# Rasie Keyerror ---- 


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Can't exceed over 3 meters")

bmi= weight/ height ** 2
print(bmi)

    
