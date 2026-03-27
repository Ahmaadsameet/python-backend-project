from fastapi import APIRouter

user = APIRouter()

@user.get("/users")
def get_user():
    return["user","user"]

@user.post("/users")
def post_user():
    return{"message":"user created"}

@user.put("/users")
def update_user():
    return{"message":"user updated"}

@user.delete("/users")
def delete_user():
    return{"message":"user deleted"}
