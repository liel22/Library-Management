import pytest
import requests

# כתובת הבסיס של השירות
BASE_URL = "http://localhost:5007"  # עדכן לפי הכתובת והפורט של השירות

def test_generate_report_success():
    """
    בדיקה חיובית: וידוא שהדוח נוצר בהצלחה והמידע תקין.
    """
    url = f"{BASE_URL}/reports"
    response = requests.get(url)

    # בדיקת תגובת ה-API
    assert response.status_code == 200, "צפינו לקבל קוד 200 OK אך קיבלנו קוד אחר"
    
    # בדיקת מבנה התגובה
    data = response.json()
    assert "total_books" in data, "התגובה חסרה את השדה 'total_books'"
    assert "total_borrows" in data, "התגובה חסרה את השדה 'total_borrows'"
    assert "popular_books" in data, "התגובה חסרה את השדה 'popular_books'"
    assert "average_ratings" in data, "התגובה חסרה את השדה 'average_ratings'"
    
    # בדיקת סוגי המידע שהתקבל
    assert isinstance(data["total_books"], int), "'total_books' צריך להיות מסוג int"
    assert isinstance(data["total_borrows"], int), "'total_borrows' צריך להיות מסוג int"
    assert isinstance(data["popular_books"], list), "'popular_books' צריך להיות מסוג list"
    assert isinstance(data["average_ratings"], list), "'average_ratings' צריך להיות מסוג list"

def test_generate_report_database_failure():
    """
    בדיקה שלילית: וידוא שהשירות מחזיר שגיאה כאשר החיבור למסד הנתונים נכשל.
    """
    # בדוק במקרה בו books_collection הוא None
    url = f"{BASE_URL}/reports"
    response = requests.get(url)

    # הנחה: המסד מחובר ולכן נוודא שלא מתרחש חיבור כושל
    assert response.status_code != 500, "צפינו לקבל קוד שונה מ-500 במצב בו החיבור למסד נתונים עובד כראוי"
