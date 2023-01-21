from flask import Flask
from pymongo import MongoClient
# env imports
from dotenv import load_dotenv
import os


load_dotenv()
MONGO=os.getenv("MONGO")



app = Flask(__name__)
# import secrets
# secrets.token_hex(20)
app.config["SECRET_KEY"] = "035aacc41cf96068fc072dbba659d732b5e0994d"

MONGO_URL = MONGO
mongodb_client = MongoClient(MONGO_URL)
db = mongodb_client["FlaskTodo"]
todo = db["Todo"]


from . import routes 