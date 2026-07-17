words = ['apple','ball','cat','dog']


print("The words are ",words)


words.append("Egg")   #append only add single item 

print("The words are ",words)
#To add multiple items 


words.extend(["Fish" , "Giraffe"])

print(words)

print(words[0])

#Tupels in python


cordinates =  (12,1)

print ("cordinates are ",cordinates)

#sets

uniqueNumbers = {1,2,3,3}
print(uniqueNumbers)


#dictionaries
student = {
    "name" : "Raman",
    "age":22
}

print(student)

fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[-1])
languages = ["Python", "JavaScript"]

print(languages.append("Go"))


# exercise 1
name = []
name.append("Raman")
name.append("Mbappe")
name.append("Ronaldo")
name.append('Neymar')


print("Name ",name)


#practice shopping Cart

cart  = ["Laptop"]
cart.append("Mouse")
cart.append("Keyboard")


print("cart" ,cart)


notifications = ["Welcome!" ," Order shipped", "Order delivered"]

print(notifications[0])


#count products

products = ["Laptop",
    "Phone",
    "Tablet",
    "Watch",
    "Camera"]




print(len(products))


skills = [
    "Python",
    "FastAPI",
    "PostgreSQL"
]


if("Python" in skills):
    print("found")
else:
    print("notFound")
    
    
    
    
    