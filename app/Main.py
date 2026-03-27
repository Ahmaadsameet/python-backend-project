from fastapi import FastAPI

app=FastAPI()

@app.GET("/")
def read_root():
    return{"hello":"world"}



