import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

USERNAME="sahithiaekka"
token_key= os.getenv("TOKEN")
GRAPH_ID="graph1"

# print(token_key)
pixela_endpoint= "https://pixe.la/v1/users"

user_parms={
    "token": token_key,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# ......create an user account .........
# response= requests.post(url=pixela_endpoint,json=user_parms) 
# print(response.text)
# Respones --{"message":"Success. Let's visit https://pixe.la/@sahithiaekka , it is your profile page!","isSuccess":true}

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config= {
    "id": GRAPH_ID,
    "name":"walking",
    "unit":"Km",
    "type":"float",
    "color":"ichou"   
}

headers = {"X-USER-TOKEN" :token_key }

# ........create a graph.......
# response=requests.post(url= graph_endpoint, json=graph_config, headers=headers)
# print(response.text) #{"message":"Success.","isSuccess":true}

today= datetime(year=2025, month=6, day=20)
# print(today)



pixel_craetion_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#create a request body 
pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"4",
}

# # ...........creat pixel data.....
# response=requests.post(url=pixel_craetion_endpoint, json=pixel_data, headers=headers)
# print(response.text)
# # {"message":"Success.","isSuccess":true}-- output 
# strftime- string f time method 

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)
# {"message":"Success.","isSuccess":true}- Output 

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)


# https://pixe.la/v1/users/sahithiaekka/graphs/graph1.html----- URL 