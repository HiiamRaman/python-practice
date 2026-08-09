# from fastapi import FastAPI, Depends


# app = FastAPI()


# def provide_message(name):
#     print("Hello from dependecy")
#     return f"Hello {name} from dependency"


# @app.get("/demo")
# def demo(message: str = Depends(provide_message)):
#     print("Now route is executed")
#     return message


# #


# from fastapi import FastAPI, status, HTTPException, Depends, Header

# app = FastAPI()


# users = {
#     1: {
#         "id": 1,
#         "name": "Raman",
#         "role": "user",
#     },
#     2: {
#         "id": 2,
#         "name": "Alex",
#         "role": "admin",
#     },
# }


# def get_user(userId: int):
#     print("Hi i am dependency")
#     user = users.get(userId)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


# @app.get("/user", status_code=status.HTTP_201_CREATED)
# def get_profile(currentuser: dict = Depends(get_user)):
#     print(currentuser)
#     return currentuser


# def verify_api_key(x_api_key: str = Header()):
#     if x_api_key != "secret123":
#         raise HTTPException(status_code=400, detail="Invalid Api key")
#     return x_api_key


# @app.get("/protected")
# def header_demo(api_key: str = Depends(verify_api_key)):
#     return {"received_key": api_key, "success": "Access Grantted"}

