from turtle import Turtle 

a=["red","green", "blue", "yellow"]

print("output 1")
for i in a:
    print(i)

print("output 2")
for i in range(0,len(a),1):
    print(i)

print("output 3")
for i in range(0,len(a),1):
    print(a[i])

print("output 4")
for i, value in enumerate(a):
    print(f"Index is {i} and value is {value}")
    turtle_object= Turtle()
    turtle_object.color(value)
    print(turtle_object.color())
    
print(a.index("yellow"))
    
    

