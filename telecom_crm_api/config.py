import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    DATA_FILE = 'users.json'  # JSON file path for storing user data
