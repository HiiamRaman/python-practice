from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello Developer"}


@app.get('/user')
def create_user():
    return { 'message':'User created successfully'}

@app.get('/user/{user_id}')
def get_user(user_id:int):
    return {
        'message':f' user number {user_id} is found',
        'user_id':user_id
    }
    
    #create a route that returns bok id 
@app.get('/books/{book_id}')
def get_bookid(book_id:int):
    return {
        'bookid':f'The id of book is {book_id}'
    }



#create a route that returns stdent id 

@app.get('/students/{student_id}')
def get_studentid (student_id):
    return {
        'studentId ' : f"the given student is {student_id}"
    }
    
    
@app.get('/about')
def about ():
    return {
        'message':'Wecome to About Page'
    }
    
#handling two  parameter data


@app.get('/user/{userid}/order/{orderid}')
def getorder(userid:int,orderid:int):
    return {
        'message':f'the user is {userid} ',
        'orderid':f'ther order id is  {orderid}'
    }
    
    
    # /products/{product_id}/reviews/{review_id}
    
@app.get('/products/{product_id}/reviews/{review_id}')
def product_review (product_id:int, review_id:int):
    return {
        'product_id': f'the product id is {product_id} ',
        'review_id':f'the review id is {review_id}'
    }
     