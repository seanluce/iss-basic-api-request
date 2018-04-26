import json
import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
data = response.json()
print(data["iss_position"]["latitude"])
print(data["iss_position"]["longitude"])
