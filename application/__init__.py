from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
# import secrets
# secrets.token_hex(20)
app.config["SECRET_KEY"] = "035aacc41cf96068fc072dbba659d732b5e0994d"

MONGO_URL = "mongodb://admin:admin@ac-auxs7ka-shard-00-00.protkog.mongodb.net:27017,ac-auxs7ka-shard-00-01.protkog.mongodb.net:27017,ac-auxs7ka-shard-00-02.protkog.mongodb.net:27017/?ssl=true&replicaSet=atlas-ljpoe4-shard-0&authSource=admin&retryWrites=true&w=majority"
mongodb_client = MongoClient(MONGO_URL)
db = mongodb_client["FlaskTodo"]
todo = db["Todo"]


from . import routes 