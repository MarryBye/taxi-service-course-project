import os
from os import path
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

DB_SUPER_USER = os.getenv("DB_SUPER_USER")
DB_SUPER_PASSWORD = os.getenv("DB_SUPER_PASSWORD")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_TOKEN_LIFETIME = int(os.getenv("JWT_TOKEN_LIFETIME", 30)) 