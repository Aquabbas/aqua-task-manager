# MongoDB driver for local MongoDB (and Async Communication) Server
import motor.motor_asyncio
from model import Todo

# For the connection between database.py and Local MongoDB Server
# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')

from decouple import config
# For the connection between database.py and Remote MongoDB Server
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# uri = "mongodb+srv://abbashayder:xZIVEPhGdXzJjLBG@aquataskmanager.irrlazq.mongodb.net/?retryWrites=true&w=majority"
uri = config('uri')


# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
client = MongoClient(uri, server_api=ServerApi('1')) # type: ignore


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Name of the database is "TodoList"
database = client.TodoList

# Collection = is what a Table is in SQL --> Name of Table is "todo"
collection = database.todo


async def fetch_one_todo(title):
    document = collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = collection.insert_one(document)
    return document

async def update_todo(title, desc):
    collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = collection.find_one({"title": title})
    return document

async def remove_todo(title):
    collection.delete_one({"title": title})
    return True