from fastapi import APIRouter

router = APIRouter()

@router.get("/orders")
def get_order():
    return["order","order"]

@router.post("/orders")
def post_order():
    return{"message":"order created"}

@router.put("/orders")
def update_order():
    return

@router.delete("/orders")
def delete_order():
    return{"message":"order deleted"}