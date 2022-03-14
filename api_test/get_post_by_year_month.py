import requests
# provide year and month from keyboard
param = {"year": input(), "month" : input()}
params_value = {'page': 1, 'bool': 'true', 'per_page': 10}
response = requests.get("http://localhost:8888/api/blog/posts/archive/{year}/{month}".format(**param),
                        params=params_value)
print(response.json())
status_code = response.status_code
status = str(status_code)

try:
    assert status_code == 200
    print("status_code is " + status)
except AssertionError as status_error:
    print("status code is " + status, "Get request is not successful")
