import uuid
import pytest
import requests

# כתובת הבסיס של השירות
BASE_URL = "http://localhost:5004"  # עדכן לפי הצורך
BASE_URL2 = "http://books-add:5002"

def test_borrow_book_success():
    random_title = f"Book-{uuid.uuid4()}"
    # הוספת הספר לפני ההשאלה
    requests.post(f"{BASE_URL2}/add_book", json={
        "title": random_title,
        "author": "Author Name",
        "category": "Fiction",
    })

    #borrow the book
    response = requests.post(f"{BASE_URL}/borrow-book", json={
        "username": "kobi",
        "title": random_title
    })
    assert response.status_code == 200, "failed to borrow a book"
    assert response.json()["message"] == "Book borrowed successfully"


def test_borrow_book_nonexistent_book():
    """
    negative test case for borrowing a nonexistent book
    """
    url = f"{BASE_URL}/borrow-book"
    payload = {
        "username": "kobi",  
        "title": "Nonexistent Book"  
    }
    response = requests.post(url, json=payload)

    # בדיקת תגובת ה-API
    assert response.status_code == 404, "failed to borrow a nonexistent book"
    assert response.json()["error"] == "Book not found"
