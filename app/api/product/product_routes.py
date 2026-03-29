from fastapi import APIRouter
from app.api.product import product_service
router = APIRouter()

@router.get("/products")
def get_products():
    return product_service.get_all_products()
 
@router.get("/products/{id}")
def get_product(id:int):
    return product_service.get_product_by_id(id)

@router.post("/products")
def create_product(name: str, price: float):
    return product_service.create_product(name=name, price=price)

@router.put("/products/{id}")
def update_product(id:int,name:str):
    return product_service.update_product(product_id=id,name=name) 

@router.delete("/products/{id}")
def delete_product(id:int):
    return product_service.delete_product(product_id=id)
  