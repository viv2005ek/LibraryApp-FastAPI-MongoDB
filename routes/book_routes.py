from fastapi import APIRouter, HTTPException, status
from models.book_model import (
    get_all_books,
    get_book_by_id,
    add_book,
    update_book,
    delete_book,
)
from schemas.book_schema import BookCreate, BookUpdate, BookOut
from typing import List

router = APIRouter()

# ✅ GET all books
@router.get("/books", response_model=List[BookOut])
async def read_all_books():
    return await get_all_books()

# ✅ GET a single book by ID
@router.get("/books/{book_id}", response_model=BookOut)
async def read_book(book_id: str):
    book = await get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# ✅ POST - Add a new book
@router.post("/books", response_model=BookOut, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate):
    return await add_book(book)

# ✅ PUT - Update a book
@router.put("/books/{book_id}", status_code=status.HTTP_200_OK)
async def edit_book(book_id: str, updated_data: BookUpdate):
    updated = await update_book(book_id, updated_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found or nothing to update")
    return {"message": "Book updated successfully"}

# ✅ DELETE - Remove a book
@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_book(book_id: str):
    deleted = await delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return
