# Class inheritence: classes can inheritance from classes iherting attributies, methods 

#  How does it work?? -- super.int - super refers to the supper class 

class Animal:
    def __init__(self):
        self.num_eyes =2
    
    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__() #while writing this it came up by itself 
        # 
    
    def breathe(self):
        super().breathe()
        print("Doing this under water.")
    
        
    def swim(self):
        print("Is swimming in water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# Objectted created from fish class no has access to all the attributes and methods from the super class 

# ******** SLICING LIST ************ 

       