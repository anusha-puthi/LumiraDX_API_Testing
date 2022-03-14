import datetime
import requests
import json

# create a post using a post request
print(datetime.datetime.now())
API_endpoint = 'http://localhost:8888/api/blog/posts/'
payload = {
         "id": 15,
         "title": "Lumira post 2",
         "body": "Testing Post request",
         "pub_date": "2022-03-12T16:18:35.674Z",
         "category_id": "1",
         "category": "sci-Fi"
         }

# Assigning headers to take json format
headers = {"Content-Type": "application/json"}
# packing post request with json body
response = requests.post(API_endpoint, headers=headers, data=json.dumps(payload))
print(response.json())
try:
    assert response.status_code == 201
    print(response, "status code is matching")

except:
    print("Status code not matching, Post is not successful")


#  validating the response headers
print(response.headers)
headers = response.headers
print(headers)
# validating the headers
if headers.get("Content-Type").__contains__("json"):
    print("Response is in Json format")
else:
    print("Response is not in Json format")


