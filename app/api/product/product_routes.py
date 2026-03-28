from fastapi import APIRouter
router = APIRouter()

@router.get("/products")
def get_products():
    return["item","item"]

@router.get("/products,/{id}")
def get_product(id:int):
    return{"item_id":id,"name":"item name"}

@router.post("/products")
def create_product():
    return{"message":"product created"}

@router.put("/products")
def update_product():
    return{"message":"product updated"}

@router.delete("/products")
def delete_product():
    return{"message":"product deleted"}
