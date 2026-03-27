from fastapi import APIRouter
router = APIRouter()

@router.get("/products")
def get_product():
    return["item","item"]

router.post("/products")
def create_product():
    return{"message":"product created"}

router.put("/products")
def update_product():
    return{"message":"product updated"}

router.put("/products")
def delete_product():
    return{"message":"product deleted"}

router.delete("/products")
def delete_product():
    return{"message":"product deleted"}