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


from fastapi import FastAPI, status, HTTPException, Depends, Header

app = FastAPI()


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

# from fastapi import FastAPI, Header, status, HTTPException, Depends


# app = FastAPI()


# users = {
#     "userkey": {
#         "id": 1,
#         "name": "Raman",
#         "role": "user",
#     },
#     "adminkey": {
#         "id": 2,
#         "name": " Raman",
#         "role": "admin",
#     },
# }


# # Authentication Dependency


# def get_current_user(key: str = Header()):
#     print("Authentication dependecy executed")
#     user = users.get(key)
#     if user == None:
#         raise HTTPException(status_code=401, detail="Invalid Key")
#     return user


# # Authorization dependency


# def require_admin(current_user: dict = Depends(get_current_user)):
#     print("Authorization dependency executed")
#     if current_user["role"] != "admin":
#         raise HTTPException(status_code=403, detail="Admin is required  ")
#     return current_user["name"]


# @app.get("/admin/dashboard")
# def admin_dashboard(user: str = Depends(require_admin)):
#     return {"message": "Welcome to admin dashboard ", "User": f"Admin {user}"}


users_by_api_key = {
    "user-key": {
        "id": 1,
        "name": "Raman",
        "role": "user",
    },
    "admin-key": {
        "id": 2,
        "name": "Admin Raman",
        "role": "admin",
    },
}


# Authentication dependency


def get_current_user(x_api_key: str = Header()):
    user = users_by_api_key.get(x_api_key)
    if user is None:
        raise HTTPException(status_code=403, detail="invalid api key")

    return user


def require_admin(user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=401, detail="Admin required !!!!")
    return user


@app.get("/admin/dashboard")
def admin_dashboard(current_admin: dict = Depends(require_admin)):
    print("Route executed")
    return {"message": "Welcome Admin", "user": current_admin['name']}
