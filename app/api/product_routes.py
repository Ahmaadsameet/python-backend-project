from fastapi import APIRouter
router = APIRouter()

@router.get("products")
def get_product():
    return["item","item"]

router.post("products")
def create_product():
    return{"message":"product created"}
 