# create a dictionary

student  = {
    
    "name":"Raman",
    "age":23,
    "course":"Ai"
}




#print 23 
print(student["age"])

# update value

student["course"]  = "AI & Computational Intelligence "

print (student)



student ['school'] = "none"
print (student)

# delete a key
del student["school"]

print (student)

for item in student:
 print (student[item])
 
 
if("age" in student):
     print("age found")
else :
     print('age not found')    
     
     
     
     
if ('course' in student):
    print ('course is found')
    
scores   = {'alice':99, 'bob':98, 'ram':100}


highestMark = max(scores.values())
print(highestMark)