# API -- APPLICATION PROGRAM INTERFACE 

# a set of functions protocols and objects that programers can use to create software or interact with an external system 
# think of it as a bridge or interface between your program and external data sources or services.


# 🔁 How APIs Work
# You send a request to the API (e.g., "What's the weather in Flint today?").
# The request must follow the API's format and rules (defined in the API documentation).
# If correct, the API will respond with the requested data.
# If incorrect, you’ll get an error message.


# 📍 What Is an API Endpoint?
# An API endpoint is the URL (web address) where data is accessed.
# It’s like the address of a bank — if you want to withdraw data (like money), you need to know where to go.
# Example:  To get crypto data: https://api.coinbase.com
# To get the ISS current location: http://api.open-notify.org/iss-now.json


# Making an API Request: 
# Use the requests Python library to make the request.
# Call the get() method with the endpoint URL.
# Store the response in a variable.

# JSON (JavaScript Object Notation) is the format used for data exchange via APIs. It's lightweight, minimal, and structured like. {"quote":"this is an example"}, its data structure is a dictionary

# Error Codes
# '404'  error code :  Dosen't exit the program that you're looking for dosen't exist 
#  200 means OK, i.e., your program: Connected to the API endpoint, Made a valid request and Received a proper response from the server

#  1XX-- Hold on 
#  2XX-- works , here you go 
#  3XX-- You don't have the permision to get this 
#  4XX-- You screwed up , dosen't work 
#  5XX-- SServer screwed up , server issues 

# Webpage: httpstatuses.com - gives you all the response codes 

# API PARAMETERS 
# not all api's have parameters  


