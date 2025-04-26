import json

# Python dictionary (similar to JSON object)
person = {
    "name": "John",
    "age": 30,
    "isStudent": True
}


# Convert Python object to JSON string
json_string = json.dumps(person)
print("JSON String:", json_string)

# Convert back to Python object
python_object = json.loads(json_string)
print("\nPython Object:", python_object)
print("Type:", type(python_object))

restraunt ={
    "name": "Noori pocha",
    "cuisineType": "Korean",
    "popularDishes": ["chickenbulgogi", "fried chicken", "soju"]
}

with open('restraunt.json', 'w') as file:
    json.dump(restraunt, file, indent=4)
    
with open('restraunt.json','r') as file:
    loaded_data = json.load(file)
    print("\nLoaded Data", loaded_data)
    