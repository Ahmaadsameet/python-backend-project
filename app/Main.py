from fastapi import FastAPI
from app.api.product.product_routes import product 
from app.api.user.user_routes import user 
from app.api.order.order_routes import order 


app=FastAPI() 

app.include_router(product)
app.include_router(user)
app.include_router(order)


@app.get("/")
def read_root():
    return{"hello":"api running"}



