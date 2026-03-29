order_db =[
    {
        "id": 1,
        "item":[
            {"product_id": 1, "quantity": 2},
            {"product_id": 2, "quantity": 1}
        ],
        "total_proce":float,
        "status":str  

    }

]

def get_all_orders():
    return order_db

def get_order_by_id(order_id:int):
    for order in order_db:
        if order["id"] == order_id:
            return order
    return {"message": "order not found"}

def create_order(items:list):
    total_price = sum(item["quantity"] * 10.0 for item in items) 
    new_order = {
        "id": len(order_db) + 1,
        "item": items,
        "total_price": total_price,
        "status": "pending"
    }
    order_db.append(new_order)
    return new_order

def update_order_status(order_id:int,status:str):
    for order in order_db:
        if order["id"] == order_id:
            order["status"] = status
            return order