# Create a list of 5 fruits and print each fruit with its index number.


fruits = ["mango", "apple", "banana", "orange", "grapes"]

for item, fruit in enumerate(fruits):
    print(item, fruit)


friends = ["raman", "raman", "raman", "raman"]


for index, friend in enumerate(friends):
    print(index, friend)


# Make a dictionary of 3 countries and their capitals. Then write code to print:

countries = [
    {"country": "Nepal", "capital": "Kathmandu"},
    {"country": "india", "capital": "delhi"},
    {"country": "china", "capital": "beijing"},
]


for index, country in enumerate(countries, start=1):
    print(f"{index}.  Country name is  {country["capital"]}")


students = [
    {"name": "Ram", "marks": 85},
    {"name": "Hari", "marks": 72},
    {"name": "Sita", "marks": 95},
    {"name": "Gita", "marks": 68},
]

for index, marks in enumerate(students, start=1):
    print(f" {index}. {marks['name']}  scored {marks['marks']}")


#     Write a function square(n) that returns the square of a number.
# Test it with square(5) → should return 25.


def square(number):
    return number * number


print(" the square of the number is ", square(10))


def add(a: int, b: int) -> int:
    return a + b


print(add(2, 3))


def sum(a: str, b: str) -> str:
    return a + b


print(sum("1", "2"))


def output(name: str) -> str:
    print(f" i am a {name}")


output("software Developer")


products:list[str] = ["Laptop", "Phone", "Tablet"]

def getProducts(products : list[str] ) :
     return products
    


print(getProducts(products))
    
    
        
