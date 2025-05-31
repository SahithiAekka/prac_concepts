class User:
    def __init__(self,id,name):
        print("new user being created...")
        self.id= id
        self.username= name
        self.followers = 0
        self.following = 0
        
    def follow(self,user):
       

# user_1= User()
# user_1.id = "001"
# user_1.name= "Sahithi"


user_1=User("001","Sathvik")
# Attribbute is a variable that is associated with the object 

# PascalCase -- used for class names 
# camelCase -- not used alot in python 
# snake_case -- used for all most everything 


# how to specify what should happen when your obejct is being created 
# iniatlizing the or cretating the starting values for the 

print(user_1.name)
print(user_1.id)

# ATTRRIBUTES ARE THE THINGS THAT THE OBJECT HAS AND METHODS ARE THE THINGS THAT THE OBJECT DOES
# WHEN A FUNCTION IS ATTACHED TO AN OBJECT THEN ITS CALLED A METHOD 

# created a method secret name 
User.follow("user_2","002","Jatin")

print()