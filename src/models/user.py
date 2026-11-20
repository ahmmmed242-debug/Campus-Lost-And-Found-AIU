
class User:
    def __init__(self, user_id: int, name: str, email: str, phone: str, role: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.role = role

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Role: {self.role}"
