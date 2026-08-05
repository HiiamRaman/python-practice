from pydantic  import BaseModel
class Book(BaseModel):
    title:str
    price:float
    pages:int
    available:bool = True
book = Book(
     title='science',
     price=23,
     pages=12,

)
