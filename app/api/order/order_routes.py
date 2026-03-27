from fastapi import APIRouter

order = APIRouter()

@order.get("/orders")
def get_order():
    return["order","order"]

@order.post("/orders")
def post_order():
    return{"message":"order created"}

@order.put("/orders")
def update_order():
    return

@order.delete("/orders")
def delete_order():
    return{"message":"order deleted"}