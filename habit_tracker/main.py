import requests
import os

USERNAME="sahithiaekka"
token_key=os.getenv("TOKEN")


pixela_endpoint= "https://pixe.la/v1/users"

user_parms={
    "token": token_key,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}


# response= requests.post(url=pixela_endpoint,json=user_parms) # create an user account 
# print(response.text)
# Respones --{"message":"Success. Let's visit https://pixe.la/@sahithiaekka , it is your profile page!","isSuccess":true}

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config= {
    "id":"graph1",
    "name":"walking",
    "unit":"Km",
    "type":"float",
    "color":"ichou"   
}

headers = {"X-USER-TOKEN" :token_key }

# response=requests.post(url= graph_endpoint, json=graph_config, headers=headers)
# print(response.text) #{"message":"Success.","isSuccess":true}
