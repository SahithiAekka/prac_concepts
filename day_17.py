class User:
    def __init__(self,id,name): 
        # a constructor sets up what variables should go in the class without errors. 
        # you can sometimes give default values to the variebles 
         
        self.id= id
        self.username= name
        self.followers = 0
        self.following = 0
        
    def follow(self,user):
        user.followers +=1
        self.following +=1
       

# user_1= User()
# user_1.id = "001"
# user_1.name= "Sahithi"

# how to specify what should happen when your obejct is being created 
# iniatlizing the or cretating the starting values for the  this helps in not having errors by mistakely changing while creating users 


user_1=User("001","Sathvik")

# Attribbute is a variable that is associated with the object 

# PascalCase -- used for class names 
# camelCase -- not used alot in python 
# snake_case -- used for all most everything 


# ATTRRIBUTES ARE THE THINGS THAT THE OBJECT HAS AND METHODS ARE THE THINGS THAT THE OBJECT DOES
# WHEN A FUNCTION IS ATTACHED TO AN OBJECT THEN ITS CALLED A METHOD it need a self 

user_2=User("002", "Jatin")

print(user_1.following)
print(user_2.followers)

user_1.follow(user_2)


print(user_1.following)
print(user_2.followers)