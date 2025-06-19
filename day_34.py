# How API authnetication works?? 
# API KEy is almost like a personal password 

import requests

# Current weather data: 
url = "https://api.openweathermap.org/data/2.5/weather?q=Flint,USA&appid=170d8e5582466908638073c4c6e01057"
response_current = requests.get(url)
print(response_current.status_code)
print(response_current.json())

# converting important keys into enviromnet variables 
# dir Env:
# $env:OPENWEATHERMAP_API_KEY = "the key"
# echo $env:OPENWEATHERMAP_API_KEY
