import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_KEY = os.getenv("MHDBLOCKCHAIN_API_KEY")
    NODE_URL = os.getenv("MHDBLOCKCHAIN_NODE_URL")
