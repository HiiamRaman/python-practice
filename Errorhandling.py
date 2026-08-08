from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


# products = {
#     1: {"id": 1, "name": "Laptop"},
#     2: {"id": 2, "name": "Phone"},
# }


# @app.get("/products/{product_id}")
# def get_product(product_id: int):
#     product = products.get(product_id)
#     if product is None:
#         raise HTTPException(status_code=404, detail="Product not found !!!")


#     return product
class UserRegister(BaseModel):
    name: str
    email: str
    password: str


registered_emails = {"admin@gmail.com"}


@app.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: UserRegister):
    if user.email in registered_emails:
        raise HTTPException(status_code=409, detail="User already exists")
    registered_emails.add(user.email)
    print("registered_emails", registered_emails)

    return {"name": user.name, "email": user.email}
