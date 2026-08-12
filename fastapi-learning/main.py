from fastapi import FastAPI
from routers.users import router as user_router
from routers.products import router as product_router
app = FastAPI()
app.include_router(user_router)
app.include_router(product_router)

@app.get("/")
def home():
    return "FastAPI application running"
