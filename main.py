from fastapi import FastAPI

from app.api.product.routes import router as product
from app.api.user.routes import router as user
from app.api.order.routes import orouter as order


app=FastAPI() 

app.include_router(product)
app.include_router(user)
app.include_router(order)


@app.get("/")
def read_root():
    return{"hello":"api running"}



