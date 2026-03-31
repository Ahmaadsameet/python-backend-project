class userService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create_user(self, user_data):
        return self.user_repository.create(user_data)

    def get_user(self, user_id):
        return self.user_repository.get_by_id(user_id)

    def update_user(self, user_id, user_data):
        return self.user_repository.update(user_id, user_data)

    def delete_user(self, user_id):
        return self.user_repository.delete(user_id)
