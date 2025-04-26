import json

# Python dictionary (similar to JSON object)
person = {
    "name": "John",
    "age": 30,
    "isStudent": True
}

# Convert Python object to JSON string
json_string = json.dumps(person)
print(json_string)