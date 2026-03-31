from fastapi import APIRouter
from app.services.product_service import productService
service = productService()
 
router = APIRouter()

@router.get("/products")
def get_products():
    return service.get_all_products()
 
@router.get("/products/{id}")
def get_product(id:int):
    return service.get_product_by_id(id)

@router.post("/products")
def create_product(name: str, price: float):
    return service.create_product(name, price)

@router.put("/products/{id}")
def update_product(id:int,name:str):
    return service.update_product(product_id=id,name=name) 

@router.delete("/products/{id}")
def delete_product(id:int):
    return service.delete_product(product_id=id)
  