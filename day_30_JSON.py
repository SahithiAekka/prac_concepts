# JSON - Java Script Objet Notation 
# it has a simple structure , 
# Composed of a bunch of nested lists and dictionaries and it has key value pair data structure 

# WRITE _ json.dump() 

# READ __ json.load()

# UPDATE __ json.update()

# JSON is built on two structures:

# Objects: In JSON, objects are unordered sets of key/value pairs
{
  "name": "Sahithi",
  "age": 25,
  "isStudent": False
}

# Arrays: Ordered list of values. Written in [ ] square brackets

["apple", "banana", "cherry"]

import json

# Convert Python dict to JSON string
data = {"name": "Sahithi", "age": 25}
json_string = json.dumps(data)

# Convert JSON string back to Python dict
parsed_data = json.loads(json_string)


#  Real-Life Use: Web APIs return data in JSON format, Config files (e.g., package.json in Node.js), Storing structured data (like user profiles)