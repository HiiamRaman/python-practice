# import requests


# res = requests.get("https://jsonplaceholder.typicode.com/users")

# print("Status Code:", res.status_code)


# data = res.json()
# print(data[0]["name"])


# def division():
#     try:
#         print("Opening Application")
#         number = 10 / 0
#         print(f"the number is {number}")
#     except ZeroDivisionError:
#         print("cannot divide by 0")
#     else:
#         print("Everything executed successfully")

#     finally:
#         print("Program run successfully")


# # division()


# # Raising ypur own exception


# # age = int(input("Enter Age "))
# # if (age<19):
# #     raise Exception(' you are little boy')
# # else:
# #     print(' You are man now ')


# def login(username, password):
#     if username != "Raman" and password != "12345678":
#         raise Exception("Username is invalid")

#     else:
#         print(f"User login is successfull {username}")


# login("Raman", "12345678")


# # division
# def division_example():
#     try:
#         num = int(input("Enter a number "))
#         print(num / 10)
#     except ValueError:
#         print(" Enter a valid number")


# division_example()


# student = {"name": "Raman", "age": 24}


# key = input("Enter a key")


# # if(key in student):
# #     print(student[key])

# # else:
# #     print('Invalid Key')


# if key in student and student[key] == key:
#     print(student[key])



# numbers = [1,2,3,4,5,6,7,8]
# def display ():
#     try:
#         index = int(input('Enter a index'))

#         print(numbers[index])
#     except ValueError:
#         print('enter a valid number')
#     except IndexError:
#         print('Enter a valid index')
        
# display()


# #File

# def  file_read():
#     try:
#         with open("student.txt",'r')   as file:
#             print(file.read())
#     except FileExistsError:
#         print('File dont exist')
#     except FileNotFoundError:
#         print('FileNotFoundError')













# project MiniAtm

# features cheeck balannce , Deposit, Withdraw , Exit   


#check balance , withdraw , deposit, exit




def atm_work ():
    try:
         choice = int(input('Choose a option  '))
         
         print (f"You have choosen {choice }")
         
         if(choice==1):
             print("Checking balance..")
         elif(choice==2):
            print('Depositing money...')
         elif(choice==3):
             print("Withdrawing money...")
         elif(choice==4):
             print("Good Bye")
         else: 
             print(' Choose optio between 1-4')
    except ValueError:
         print(' Enter a valid option ')
         
            
atm_work()


