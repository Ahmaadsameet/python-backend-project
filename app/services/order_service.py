class orderService:
    def __init__(self):
        self.order_db =[
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

def get_all_orders(self):
    return self.order_db

def get_order_by_id(self, order_id:int):
    for order in self.order_db:
        if order["id"] == order_id: 
            return order
    return {"message": "order not found"}

def create_order(self, items:list):
    total_price = sum(item["quantity"] * 10.0 for item in items) 
    new_order = {
        "id": len(self.order_db) + 1,
        "item": items,
        "total_price": total_price,
        "status": "pending"
    }
    self.order_db.append(new_order)
    return new_order

def update_order_status(self, order_id:int,status:str):
    for order in self.order_db:
        if order["id"] == order_id:
            order["status"] = status
            return order