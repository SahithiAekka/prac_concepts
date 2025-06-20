import requests
from datetime import * 

MY_LAT = 42.652401
MY_LONG = -83.132561

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sun_rise= data["results"]["sunrise"].split("T")[1].split(":")[0]
sun_set= data["results"]["sunset"].split("T")[1].split(":")[0] #string spliting 

print(sun_rise)
print(sun_set)


current_time = datetime.now()
print(current_time.hour)