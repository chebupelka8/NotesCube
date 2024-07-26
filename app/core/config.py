import os
from dotenv import load_dotenv


load_dotenv()

if (DATABASE_URL := os.getenv("DATABASE_URL")) is None:
    print("Cannot get db url")
