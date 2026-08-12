from pydantic import BaseModel
class ProductCreate (BaseModel):
    name:str
    price:float
    quantity:int
    in_stock:bool = True


class ProductResponse (BaseModel):
    id:int
    name:str
    price:float
    quantity:int
    in_stock:bool
