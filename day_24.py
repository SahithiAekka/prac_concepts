# Opening up snake game! 

# Using Python to manage file system 

    # Open a file using open("filename.txt", mode)
    

    # Read the file using .read() or .readlines() 
        # with open("data.txt") as file:
        # content = file.read()
        # print(content)


    # Write to a file using .write() with mode 'w'
        # with open("data.txt", mode="w") as file:
        # file.write("Your new content here")


    # Append using mode 'a'
    

    # Close the file (manually with .close() or automatically with with)
    
# ABSOLUTE FILE PATH : 
    # Starts from the root directory.
    # Windows: C:/Users/Sahithi/Desktop/my_file.txt
    
    
# RELATIVE FILE PATH : talk.ppt 
    # Starts from your current working directory (where main.py is).
    # Examples:
        # ./my_file.txt → current folder
        # ../ → go up one level
        # ../../Desktop/my_file.txt → go up two levels, then down

# In Python, always use forward slashes / in file paths (even on Windows).


# ***************** MAIL MERGING PROJECT *******************************

# readlines() method returns a list containing each line in the file as a list item


# replace() method replaces a specified phrase with another specified phrase.
# string.replace(oldvalue, newvalue, count)

# strip() method removes any leading, and trailing whitespaces. Leading means at the beginning of the string, trailing means at the end.
# string.strip(characters)