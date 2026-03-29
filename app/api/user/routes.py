from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_user():
    return["user","user"]

@router.post("/users")
def post_user():
    return{"message":"user created"}

@router.put("/users")
def update_user():
    return{"message":"user updated"}

@router.delete("/users")
def delete_user():
    return{"message":"user deleted"}
