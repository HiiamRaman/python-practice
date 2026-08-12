from fastapi import APIRouter, status
from schemas.product import ProductCreate, ProductResponse

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/create", status_code=status.HTTP_200_OK, response_model=ProductResponse)
def create_product(product: ProductCreate):
    return {
        "id": 1,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
        "in_stock": product.in_stock,
    }


@router.get("/")
def get_products():
    return {"message": "All products"}


@router.get("/{product_id}")
def get_product_id(product_id: int):
    return {
        "_id": product_id,
        "name": f"product{product_id}",
        "message": "Product fetched successfully",
    }
