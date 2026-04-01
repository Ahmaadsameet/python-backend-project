class productRepostire:
    def __init__(self):
        self.product_db=[]

def add_product(self,product):
    self.product_db.append(product)
    return product   

def get_all_product(self):
    return self.product_db     


def get_product_by_id(self,product_id):
     
    for product in self.product_db:
          if product["id"] ==product_id:
               return product
    return {"error": "product not found"}

def update_product(self,product_id.updatde_product):
    for i,product in enumerate(self,db):
          if product.id== product_id:
               self.product_db[i]=update_product
               return update_product
    return None

def delete_product(self,product_id):
    for product in self.db:
          if product.id== product_id:
               self.db.remove(product)
               return True
    return False

