import requests

# provide id from keyboard
param = {"id": input()}
response = requests.delete(url="http://localhost:8888/api/blog/posts/{id}".format(**param))
print(response.status_code)

# validating the status code
try:
    if response.status_code == 204:
        print("Delete post is successful")
    elif response.status_code == 404:
        print(" Record was not found ")
except:
     print("delete post is not successful")

headers = response.headers.get("content-type")
print(headers)


