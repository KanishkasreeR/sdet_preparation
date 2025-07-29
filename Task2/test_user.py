import random
import string
from functions import validate_email_format

class TestUser:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def is_valid(self):
        return all([self.name, self.email, self.password]) and validate_email_format(self.email)
    
    @classmethod
    def generate_random_user(cls):
        name = "User" + ''.join(random.choices(string.ascii_letters, k=5))
        email = name.lower() + "@example.com"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return cls(name, email, password)
