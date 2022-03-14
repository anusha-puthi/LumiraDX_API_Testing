import requests

response = requests.get(url="http://localhost:8888/api/blog/categories/")
print(response.status_code)
# validating status code
try:
    assert response.status_code == 200
    print("get request for categories is successful ")
except AssertionError as error:
    print(error, "status is not matching")

# response in bytes
print(response.content)
# get response headers
print(response.headers)
print(response.json())

# validating the json response
json_response = response.json()
get_id = json_response[0]['id']
get_name = json_response[0]['name']
assert get_name == "Sci-Fi", get_id == 1
print(get_name, get_id)

get_id = json_response[1]['id']
get_name = json_response[1]['name']
assert get_name == "Politics", get_id == 2
print(get_name, get_id)

get_id = json_response[2]['id']
get_name = json_response[2]['name']
assert get_name == "Tech", get_id == 3
print(get_name, get_id)

#  validate the response headers
print(response.headers)
get_headers = response.headers


