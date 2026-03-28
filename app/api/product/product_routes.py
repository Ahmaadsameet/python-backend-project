from fastapi import APIRouter
router = APIRouter()

@router.get("/products")
def get_products():
    return app.api.product.product_service.get_all_products()
 
@router.get("/products/{id}")
def get_product(id:int):
    return app.api.product.product_service.get_product_by_id(id)

@router.post("/products")
def create_product():
    return app.api.product.product_service.create_product(name="new product", price=30.0)

@router.put("/products/{id}")
def update_product(id:int):
    return app.api.product.product_service.update_product(product_id=id,name="updated product")

@router.delete("/products")
def delete_product():
    return app.api.product.product_service.delete_product(product_id=1)
 