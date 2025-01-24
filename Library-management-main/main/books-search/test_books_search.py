import pytest
import requests

# כתובת הבסיס של השירות
BASE_URL = "http://localhost:5003"  # עדכן לפי הכתובת והפורט של השירות

def test_search_books_success():
    """
    בדיקה חיובית: חיפוש ספר שקיים בבסיס הנתונים
    """
    url = f"{BASE_URL}/search"
    params = {
        "title": "adam ba arava", # עדכן לשם של ספר שקיים בבסיס הנתונים שלך
        "author": "dan almog",
        "category":"kioko"

    }
    response = requests.get(url, params=params)
    
    # בדיקת תגובת ה-API
    assert response.status_code == 200, "החיפוש נכשל למרות שהספר קיים"
    assert "books" in response.json(), "צפינו למצוא רשימת ספרים בתגובה"
    assert len(response.json()["books"]) > 0, "רשימת הספרים ריקה למרות שהספר קיים"

def test_search_books_no_results():
    """
    בדיקה שלילית: חיפוש ספר שלא קיים בבסיס הנתונים
    """
    url = f"{BASE_URL}/search"
    params = {
        "title": "Nonexistent Book Title"  # שם של ספר שלא קיים בבסיס הנתונים
    }
    response = requests.get(url, params=params)
    
    # בדיקת תגובת ה-API
    assert response.status_code == 404, "צפינו שגיאה 404 כאשר הספר לא נמצא"
    assert "message" in response.json(), "צפינו לקבל הודעת שגיאה בתגובה"
    assert response.json()["message"] == "No books found matching the criteria", "הודעת השגיאה אינה תואמת את הצפוי"
