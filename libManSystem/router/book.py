from fastapi import APIRouter, HTTPException
from database import get_connection
from schemas import BookCreate, BookAction


router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/add")
def add_book(book: BookCreate):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO books (name, author, available) VALUES (?,?,1)",
        (book.name, book.author)
    )

    conn.commit()
    conn.close()
    return {"message": "Book added succcessfully"}


@router.post("/borrow")
def borrow_book(data: BookAction):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT bookId, available FROM books
        WHERE name=? AND  author=?
        """,(data.name, data.author))
    
    book =cur.fetchone()

    if not book:
        raise HTTPException(status_code=404, detail="Book not Found")
    
    cur.execute(
        "UPDATED books SET available=1 WHERE bookId=?",
        (book["bookId"],)
    )

    conn.commit()
    conn.close()
    return{"message": "Book returned successfully"}
                   
