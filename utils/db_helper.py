from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseHelper:
    client: AsyncIOMotorClient = None
    db = None

    @classmethod
    async def connect_db(cls):
        try:
            cls.client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
            cls.db = cls.client.task_manager
            await cls.client.admin.command('ping')
            print("Connected to MongoDB!")
        except ConnectionFailure:
            print("Could not connect to MongoDB")
            raise

    @classmethod
    async def close_db(cls):
        if cls.client:
            cls.client.close()
            print("MongoDB connection closed")