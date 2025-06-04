from pydantic import BaseModel
from typing import Optional

# ✅ Schema for creating a new book (used in POST /books)
class BookCreate(BaseModel):
    title: str                  # Book title (required)
    author: str                 # Author name (required)
    rating: float               # Book rating (e.g. 4.5 out of 5)
    description: str            # Short description of the book
    status: str                 # Book availability status (e.g. "available", "currently unavailable")

# ✅ Schema for updating a book (used in PUT /books/{id})
class BookUpdate(BaseModel):
    title: Optional[str] = None         # Optional field (can skip if not updating)
    author: Optional[str] = None
    rating: Optional[float] = None
    description: Optional[str] = None
    status: Optional[str] = None

# ✅ Schema for returning book data (used in GET responses)
class BookOut(BaseModel):
    id: str                     # Book ID (MongoDB ObjectId converted to string)
    title: str
    author: str
    rating: float
    description: str
    status: str
