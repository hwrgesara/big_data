import requests
import json

response = requests.get("https://api.randomuser.me/")
print(response.status_code)

parameters = {"results":10,"gender": "male", "nat": "us"}

response = requests.get("https://api.randomuser.me",
params=parameters)
print(response.text)

#Check the type of variable data
data = json.loads(response.text)
print(type(data))
print(data)

for item in data["results"]:
    print(item["name"]["first"])

space = requests.get("http://api.open-notify.org/astros.json/")
data = json.loads(space.text)
print(data)

print(data["number"])

for item in data["people"]:
    print(item["name"])
