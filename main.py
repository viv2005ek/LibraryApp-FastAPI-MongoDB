from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.book_routes import router as book_router
from models.book_model import get_all_books

# Create a FastAPI instance
app = FastAPI()

# Mount the 'static' directory to serve CSS/JS/images
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 for rendering HTML templates from the 'templates' folder
templates = Jinja2Templates(directory="templates")

# Include the book-related routes
app.include_router(book_router)

@app.get("/")
async def home(request: Request):
    books = await get_all_books()
    return templates.TemplateResponse("index.html", {"request": request, "books": books})