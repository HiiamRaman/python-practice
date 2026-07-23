# # create a dictionary

# student  = {
    
#     "name":"Raman",
#     "age":23,
#     "course":"Ai"
# }






# #print 23 
# print(student["age"])

# # update value

# student["course"]  = "AI & Computational Intelligence "

# print (student)



# student ['school'] = "none"
# print (student)

# # delete a key
# del student["school"]

# print (student)

# for item in student:
#  print (student[item])
 
 
# if("age" in student):
#      print("age found")
# else :
#      print('age not found')    
     
     
     
     
# if ('course' in student):
#     print ('course is found')
    
# scores   = {'alice':99, 'bob':98, 'ram':100}


# highestMark = max(scores.values())
# print(highestMark)



# marks = {'ram':102,'shyam':101,'hari':104}
# results=  min(marks.values())

# print(results)









employees = {
    "emp1": {
        "name": "Ram",
        "salary": 50000
    },
    "emp2": {
        "name": "Hari",
        "salary": 65000
    },
    "emp3": {
        "name": "Sita",
        "salary": 70000
    }
}


print(employees['emp1']['name'] , 'earns ' , employees["emp1"]['salary'])
print(employees["emp2"]['name'],'earns',employees["emp2"]['salary'])
print (employees["emp3"]['name'],'earns',employees["emp3"]['salary'])

name = input('enter your name')

print (name)

name1 = input("Enter your  friendly code ")
print(name1)
