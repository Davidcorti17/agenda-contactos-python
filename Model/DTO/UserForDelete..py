class UserForDelete:
    
    def __init__(self, user_id: int):
        self.user_id = user_id
    
    def __str__(self):
        return f"UserForDelete(user_id={self.user_id})"
    