import pytest
import requests
import uuid

# כתובת הבסיס של השירות
BASE_URL = "http://localhost:5005"
BASE_URL2 = "http://books-add:5002"
BASE_URL3 = "http://books-borrow:5004"

def test_return_book_success():
    """
    positive test: test the return of a book
    """
    random_title = f"Book-{uuid.uuid4()}"  # שם רנדומלי לספר

    #add the book before borrowing
    requests.post(f"{BASE_URL2}/add_book", json={
        "title": random_title,
        "author": "Author Name",
        "category": "Fiction",
    })


    requests.post(f"{BASE_URL3}/borrow-book", json={
            "username": "kobi",
            "title": random_title   
    })

    # החזרת הספר
    return_response = requests.post(f"{BASE_URL}/return-book", json={
        "username": "kobi",
        "title": random_title
    })
    assert return_response.status_code == 200, "return book failed"
    assert return_response.json()["message"] == "Book returned successfully"


