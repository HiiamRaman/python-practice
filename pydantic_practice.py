# from pydantic  import BaseModel
# class Book(BaseModel):
#     title:str
#     price:float
#     pages:int
#     available:bool = True
# book = Book(
#      title='science',
#      price=23,
#      pages=12,

# )


# from fastapi import FastAPI,status
# import fastapi
# from pydantic import BaseModel


# app = FastAPI()


# class ProductCreate(BaseModel):
#     name: str
#     price: int
#     quantity: int
#     in_stock: bool = True
# class ProductResponse (BaseModel):
#     name:str
#     price:float
#     in_stock:bool


# @app.post("/products",status_code = status.HTTP_201_CREATED,response_model=ProductResponse)
# def create_products(product: ProductCreate):
#     return {
#         "name": product.name,
#         "price": product.price,
#         "quantity": product.quantity,
#         "in_stock": product.in_stock,
#     }

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str
    role: str = "user"


class UserResponse(BaseModel):
    full_name: str
    email: str
    role: str


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_users(
    user: UserCreate,
):
    return {
        "full_name": user.full_name,
        "email": user.email,
        "password": user.password,
        "role": user.role,
    }


from fastapi import FastAPI, status
from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    name: str
    department: str
    salary: float
    is_active: bool = True


class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: str
    is_active: bool


@app.post('/employees',status_code=status.HTTP_201_CREATED,response_model=EmployeeResponse)
def creat_employee(employee:EmployeeCreate):
    return {
        "id":1,
        "name": employee.name,
        "department": employee.department,
        "salary": employee.salary,
        "is_active":employee.is_active

    }
