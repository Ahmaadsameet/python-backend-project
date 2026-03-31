from fastapi import APIRouter
from app.services.order_service import orderService
service = orderService()

router = APIRouter()

@router.get("/orders")
def get_order():
    return service.get_all_orders()

@router.post("/orders")
def post_order():
    return service.create_order(items=[{"product_id": 1, "quantity": 2}, {"product_id": 2, "quantity": 1}])

@router.put("/orders/{order_id}")
def update_order(order_id: int, status: str):
    return service.update_order_status(order_id=order_id, status=status)

@router.delete("/orders/{order_id}")
def delete_order(order_id: int):
    return service.delete_order(order_id=order_id)