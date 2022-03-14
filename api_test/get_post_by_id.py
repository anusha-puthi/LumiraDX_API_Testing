import requests

param = {"id": input()}
response = requests.get("http://localhost:8888/api/blog/posts/{id}".format(**param))
print(response.json())
status_code = response.status_code
status = str(status_code)

try:
    assert status_code == 200
    print("status_code is " + status)
except AssertionError as status_error:
    print("status code is " + status, "Get request is not successful")

#  validate the id in the response
json_response = response.json()
get_id = str(json_response["id"])
print(get_id)
get_url = response.url

if get_url.__contains__(get_id):
    print("Get post by id is successful")
else:
    print("Get post by id is not successful")

headers = response.headers
print(headers)
# validating the headers
if headers.get("Content-Type").__contains__("json"):
    print("Response is in Json format")
else:
    print("Response is not in Json format")

