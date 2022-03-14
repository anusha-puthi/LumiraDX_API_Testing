import requests

# provide year from keyboard
param = {"year": input()}
params_value = {'page': 1, 'bool': 'true', 'per_page': 10}
response = requests.get("http://localhost:8888/api/blog/posts/archive/{year}".format(**param), params=params_value)
print(response.json())

# validating the status code
status_code = response.status_code
status = str(status_code)
try:
    assert status_code == 200
    print("status_code is " + status)
except AssertionError as status_error:
    print("status code is " + status, "Get request is not successful")

# validating the response headers
headers = response.headers
print(headers)
if headers.get("Content-Type").__contains__("json"):
    print("Response is in Json format")
else:
    print("Response is not in Json format")


