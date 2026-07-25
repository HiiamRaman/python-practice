# #  create a funcrion

# def hello():
#     print('Welcome to Python!')
# hello()


# #parameter 
# def example(name):
#     print("My name is",name)
    
# example('Raman')
# example('shyam')

# #return 

# def sum (a,b):
#  return a+b




# print(sum(1,2))






# def Even (number):
#     if(number%2 == 0):
#         print('Even')
#     else:
#         print("odd")
    
# Even(2)


# def student_info(name, age, course):
#    print('student name :', name)
#    print('student age :', age)
#    print('student course :', course)
    
# student_info("Raman",23,'Ai')



def calculator(a, b, operator):
    if(operator == '+'):
        return a + b
    elif(operator == '-'):
        return a-b 
    elif(operator == '*'):
        return a*b
    else:
        return a/b
     


print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))



#Exception handling


def mul ():
    try:
        number  = int(input('Enter a number'))
        print (number)
    
    except:
        print("ENtered number  must  be integr")

mul()