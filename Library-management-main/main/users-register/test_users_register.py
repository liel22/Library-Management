import pytest
import requests
import uuid

BASE_URL = "http://users-register:5000"  # כתובת ה-API שלך

def test_register_user_success():
    """
    בדיקה חיובית: וידוא שמשתמש חדש נרשם בהצלחה.
    """
    random_username = f"user-{uuid.uuid4()}"  # יצירת שם משתמש ייחודי

    # נתוני הבקשה
    register_url = f"{BASE_URL}/register"
    response = requests.post(register_url, json={"username": random_username})

    # בדיקה אם התקבל קוד 201 (נרשם בהצלחה)
    assert response.status_code == 201, f"צפינו לקוד 201, אך קיבלנו {response.status_code}"
    data = response.json()
    assert "message" in data, "התגובה לא כוללת הודעת הצלחה."
    assert data["message"] == "User registered successfully", "הודעת ההצלחה אינה תואמת את הציפיות."
    assert "user" in data, "התגובה לא כוללת מידע על המשתמש שנרשם."
    assert data["user"]["username"] == random_username, f"המשתמש שנרשם לא תואם את {random_username}."

def test_register_user_already_exists():
    """
    בדיקה שלילית: וידוא שהמערכת מחזירה הודעה אם שם המשתמש כבר קיים.
    """
    existing_username = f"user-{uuid.uuid4()}"  # שם משתמש קיים במערכת

    # נרשום את המשתמש הראשון
    register_url = f"{BASE_URL}/register"
    response = requests.post(register_url, json={"username": existing_username})
    assert response.status_code == 201, "צפינו שהמשתמש יירשם בהצלחה בפעם הראשונה."

    # ננסה לרשום את אותו שם משתמש שוב
    response = requests.post(register_url, json={"username": existing_username})

    # בדיקה אם התקבל קוד 203 (שם המשתמש כבר קיים)
    assert response.status_code == 203, f"צפינו לקוד 203, אך קיבלנו {response.status_code}"
    data = response.json()
    assert "message" in data, "התגובה לא כוללת הודעת שגיאה."
    assert data["message"] == "Username already exists.", "הודעת השגיאה אינה תואמת את הציפיות."

