from config import book_collection
from bson import ObjectId
from schemas.book_schema import BookCreate, BookUpdate

# ✅ Helper to convert MongoDB's ObjectId to string for response
def book_helper(book) -> dict:
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "rating": book["rating"],
        "description": book["description"],
        "status": book["status"],
    }

# ✅ Get all books
async def get_all_books():
    books = []
    async for book in book_collection.find():
        books.append(book_helper(book))
    return books

# ✅ Get a single book by ID
async def get_book_by_id(book_id: str):
    book = await book_collection.find_one({"_id": ObjectId(book_id)})
    if book:
        return book_helper(book)

# ✅ Add a new book
async def add_book(book_data: BookCreate):
    new_book = await book_collection.insert_one(book_data.dict())
    created_book = await book_collection.find_one({"_id": new_book.inserted_id})
    return book_helper(created_book)

# ✅ Update a book by ID
async def update_book(book_id: str, data: BookUpdate):
    # Remove None fields from update
    update_data = {k: v for k, v in data.dict().items() if v is not None}
    if len(update_data) >= 1:
        updated = await book_collection.update_one(
            {"_id": ObjectId(book_id)}, {"$set": update_data}
        )
        if updated.modified_count > 0:
            return True
    return False

# ✅ Delete a book by ID
async def delete_book(book_id: str):
    book = await book_collection.find_one({"_id": ObjectId(book_id)})
    if book:
        await book_collection.delete_one({"_id": ObjectId(book_id)})
        return True
    return False
