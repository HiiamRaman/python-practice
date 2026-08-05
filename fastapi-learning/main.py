from fastapi import FastAPI,Query

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello Developer"}


# @app.get('/user')
# def create_user():
#     return { 'message':'User created successfully'}

# @app.get('/user/{user_id}')
# def get_user(user_id:int):
#     return {
#         'message':f' user number {user_id} is found',
#         'user_id':user_id
#     }

#     #create a route that returns bok id
# @app.get('/books/{book_id}')
# def get_bookid(book_id:int):
#     return {
#         'bookid':f'The id of book is {book_id}'
#     }


# #create a route that returns stdent id

# @app.get('/students/{student_id}')
# def get_studentid (student_id):
#     return {
#         'studentId ' : f"the given student is {student_id}"
#     }


# @app.get('/about')
# def about ():
#     return {
#         'message':'Wecome to About Page'
#     }

# #handling two  parameter data


# @app.get('/user/{userid}/order/{orderid}')
# def getorder(userid:int,orderid:int):
#     return {
#         'message':f'the user is {userid} ',
#         'orderid':f'ther order id is  {orderid}'
#     }


#     # /products/{product_id}/reviews/{review_id}

# @app.get('/products/{product_id}/reviews/{review_id}')
# def product_review (product_id:int, review_id:int):
#     return {
#         'product_id': f'the product id is {product_id} ',
#         'review_id':f'the review id is {review_id}'
#     }


# # @app.get('/products/25?include_reviews=true')
# # def get_product(product_id:int , include_reviews:bool = False):
# #     return {
# #         'product_id':25,
# #         'include_reviews':True
# #     }
# @app.get('/products/{product_id}')
# def get_product(product_id:int,include_reviews:bool  = False):
#     return {
#         "product_id":product_id,
#         'include_reviews':include_reviews

#     }


# @app.get('/products/{productId}')
# def get_productid(productId:int,include_reviews:bool=False):
#     return{
#         'productId':productId,
#         'include_reviews':include_reviews
#     }


# 1.
@app.get("/products")
def get_products(category: str='apple', limit: int = Query(default=10,ge=1,le=100), in_stock: bool = True):
    print("FUNCTION EXECUTED")

    return {"category": category, "limit": limit, "in_stock": in_stock}


# 2
@app.get("/users/{user_id}/orders")
def get_order(user_id: int, status: str = "all", limit: int = 10):
    return {"user_id": user_id, "status": status, "limit": limit}
