from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB connection URL
MONGO_DETAILS = "mongodb+srv://viv2005ek:Test123@fastapi.0mo6qni.mongodb.net/"

# Create a Motor client (asynchronous MongoDB client)
client = AsyncIOMotorClient(MONGO_DETAILS)

# Access the database named 'book_db'
database = client.book_db

# Access the collection named 'books'
book_collection = database.get_collection("books")

