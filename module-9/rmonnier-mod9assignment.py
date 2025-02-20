# Ryan Monnier
# CSD 325
# Module 9
# 19-Feb-2025

# importing requests and json
import requests
import json

# test connection 
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

# check if 200 response
if response.status_code == 200:
    print("Winner Winner!\n")
else:
    print(f"*Sad noises*: {response.status_code}")
    exit()

# unformated response
print("Raw JSON response:")
print(response.json())  # 

# format and print the api response
print("\nFormatted JSON response:")
formatted_json = json.dumps(response.json(), indent=2)
print(formatted_json)
