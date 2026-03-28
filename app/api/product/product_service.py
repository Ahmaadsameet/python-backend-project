product_db = [
    {"id": 1, "name": "product 1", "price": 10.0},
    {"id": 2, "name": "product 2", "price": 20.0},
]

def get_all_products():
    return product_db

def get_product_by_id(product_id: int):
     
     for product in product_db:
          if product["id"] ==product_id:
               return product
          return {"message": "product not found"}

def create_product(name: str, price: float):
    if not name:
     return {" error ": "name is required"}
    
    new_product = {
     "id": len(product_db) + 1,
     "name": name,
     "price": price
     
    }
    product_db.append(new_product)
    
    return new_product 

def update_product(product_id:int,name:str):
    for product in product_db:
        if product["id"] == product_id:
            product["name"] = name
            return product
    return {"message": "product not found"}

def delete_product(product_id:int):
    for product in product_db:
        if product["id"] == product_id:
            product_db.remove(product)
            return {"message": "product deleted"}
    return {"message": "product not found"}