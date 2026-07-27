import requests


res = requests.get("https://jsonplaceholder.typicode.com/users")

print("Status Code:", res.status_code)


data = res.json()
print(data[0]["name"])
