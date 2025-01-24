import pytest
import requests
import uuid
# כתובת הבסיס של השירות
BASE_URL = "http://localhost:5002"  # עדכן לפי הכתובת והפורט של השירות

def test_add_book_success():
 
    url = f"{BASE_URL}/add_book"  # עדכן את ה-Endpoint אם צריך
    random_title = f"Book-{uuid.uuid4()}"  # יצירת שם רנדומלי לספר
    payload = {
        "title": random_title,
        "author": "Author Name",
        "category": "Fiction",
        "status": "available"
    }
    response = requests.post(url, json=payload)
    
    # בדיקת תגובת ה-API
    assert response.status_code == 201, "failed to add book"
    assert "book_id" in response.json(), "missing book_id in response"

def test_add_book_missing_fields():
    url = f"{BASE_URL}/add_book"
    payload = {
        "title": "Missing Fields Book"
    }
    response = requests.post(url, json=payload)
    
    # בדיקת תגובת ה-API
    assert response.status_code == 400, "צפינו שגיאה בבקשה לא חוקית"
    assert "error" in response.json(), "צפינו שגיאה מפורטת בתגובה"

