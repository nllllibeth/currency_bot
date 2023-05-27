import os 


class Config:
    TOKEN = os.getenv("TOKEN")
    API_KEY = os.getenv('API_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')


