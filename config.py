
import random
import string
from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    
    
    key = ''.join(
        (random.choice(string.ascii_letters + string.digits + string.ascii_uppercase))
         for i in range(12))    
    
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    #SQLALCHEMY_ECHO = environ.get('SQLALCHEMY_ECHO')
    #SQLALCHEMY_ECHO = True
    #SECRET_KEY = key
    JWT_SECRET_KEY = key 
    JWT_ACCESS_TOKEN_EXPIRES = environ.get('JWT_ACCESS_TOKEN_EXPIRES')
    DEBUG = environ.get('DEBUG')