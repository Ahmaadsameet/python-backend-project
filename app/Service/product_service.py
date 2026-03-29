class productService:
    
    def __init__(self):
        self.product_db = [
    {"id": 1, "name": "product 1", "price": 10.0},
    {"id": 2, "name": "product 2", "price": 20.0},
]

def get_all_products(self):
    return self.product_db

def get_product_by_id(self,product_id: int):
     
    for product in self.product_db:
          if product["id"] ==product_id:
               return product
    return {"error": "product not found"}

def create_product(self, data :str, price: float):
    if not data:
     return {" error ": "name is required"}
    
    new_product = {
     "id": len(self.product_db) + 1,
     "name": data,
     "price": price
     
    }
    self.product_db.append(new_product)
    
    return new_product 

def update_product(self,id,data):
    for product in self.product_db:
        if product["id"] == id:
            product.update(data)
            return product
    return {"message": "product not found"}

def delete_product(self, product_id:int):
    for product in self.product_db:
        if product["id"] == product_id:
            self.product_db.remove(product)
            return {"message": "product deleted"}
    return {"message": "product not found"}