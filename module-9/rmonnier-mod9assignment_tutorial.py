# Ryan Monnier
# CSD 325
# Module 9
# 19-Feb-2025

import requests
import json

response = requests.get('http://api.open-notify.org/astros.json')
print(response.status_code)

print(response.json())

# create a formatted string of the Python JSON object
def jprint(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print(text) 

jprint(response.json())


# response = requests.get("https://api-server.dataquest.io/economic_data/countries") 
# data = response.json() 

# response = requests.get("https://api-server.dataquest.io/economic_data/countries?filter_by=region=Sub-Saharan%20Africa") 
# data = response.json()