class userService:

    def __init__(self):
        self.user_db = [
            {"id": 1, "name": "Alice", "email": "alice@example.com"}
        ]

        
        def getUser_by_id(self, user_id: int):
            for user in user_db:
                if user["id"] ==user_id:
                    return user
                
        def createUser(self,name: str,email:str):
            new_user ={
                "id":len(self.user_db) +1,
                "name":name,
                "email":email 
            }        
            self.user_db.append(new_user)
            return new_user
        
        def updateUser(self,user_id:int,name:str,email:str):
            for user in self.user_db:
                if user["id"] ==user_id:
                    user["name"] = name
                    user["email"] = email 
                    return user
            return None 
        def deleteUser(self,user_id:int):
            for user in self.user_db:
                if user["id"] ==user_id:
                    self.user_db.remove(user)
                    return {"message":"user deleted"}
            return {"message":"user not found"}