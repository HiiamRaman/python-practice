import requests


res = requests.get("https://jsonplaceholder.typicode.com/users")

print("Status Code:", res.status_code)


data = res.json()
print(data[0]["name"])


def division():
    try:
        print("Opening Application")
        number = 10 / 0
        print(f"the number is {number}")
    except ZeroDivisionError:
        print("cannot divide by 0")
    else:
        print("Everything executed successfully")

    finally:
        print("Program run successfully")




division()