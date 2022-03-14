import json

import requests
# provide id from keyboard
param = {"id": input()}
# Json payload
payload = {
             "id": 20,
              "title": "lumira test for put10",
              "body": "test for update request body",
              "pub_date": "2022-03-12T16:18:35.674Z",
              "category_id": 1,
              "category": "sci-fi"
           }
headers = {"Content-Type": "application/json"}
# packing put request with json body
response = requests.put(url="http://localhost:8888/api/blog/posts/{id}".format(**param), headers=headers,
                        data=json.dumps(payload))
#  print response
print(response)

# validating the status code
try:
    if response.status_code == 204:
        print("Post successfully updated")
    elif response.status_code == 404:
        print("Post not found")
except:
     print("put is not successful")

# printing headers
headers = response.headers
print(headers)
# validating the headers
if headers.get("Content-Type").__contains__("json"):
    print("Response is in Json format")
else:
    print("Response is not in Json format")


