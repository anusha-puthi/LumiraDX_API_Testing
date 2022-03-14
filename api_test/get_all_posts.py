import requests

params_value = {'page': 1, 'bool': 'true', 'per_page': 10}
response = requests.get("http://localhost:8888/api/blog/posts/", params=params_value)
print(response.status_code)
# validating status code
status = str(response.status_code)
try:
    assert response.status_code == 200
    print("Status code is matching and Status code is " + status)
except AssertionError as error:
    print(error, "status is not matching and status code is " + status)

#  validate the response headers
print(response.headers)

# validate the response body
response_body = response.json()
try:
    assert response_body != "null"
    print("Gte post is success")
except AssertionError as response_error:
    print(response_error)
else:
    print("Get post is not successful")

# validating the json respone
json_response = response.json()
print(json_response['total'])
print(json_response['per_page'])
get_title = json_response["items"][0]["title"]
print(get_title)

try:
    assert get_title.startswith("Title")
except AssertionError as title_error:
    print(title_error)
get_categoryid = json_response["items"][2]["category_id"]
print(get_categoryid)



