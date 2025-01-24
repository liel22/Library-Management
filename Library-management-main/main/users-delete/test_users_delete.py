import pytest
import requests
import uuid

# כתובת הבסיס של השירות
BASE_URL = "http://localhost:5001"  # עדכן לפי הכתובת והפורט של השירות
SECOND_URL = "http://users-register:5000"

def test_delete_user_success():
    """
    בדיקה חיובית: וידוא שכתובת ה-DELETE מוחקת משתמש קיים בהצלחה.
    """
    random_title = f"username-{uuid.uuid4()}"  

    # יצירת המשתמש
    register_url = f"{SECOND_URL}/register"
    register_response = requests.post(register_url, json={"username": random_title})
    assert register_response.status_code == 201, "צפינו שהמשתמש יירשם בהצלחה."

    # מחיקת המשתמש
    delete_url = f"{BASE_URL}/user_delete/{random_title}"
    delete_response = requests.delete(delete_url)

    # בדיקת תגובת ה-DELETE
    assert delete_response.status_code == 200, f"צפינו למחיקת המשתמש {random_title} בהצלחה, אך קיבלנו שגיאה."
    data = delete_response.json()
    assert "message" in data, "צפינו להודעה על הצלחה בתגובה."
    assert data["message"] == f"user '{random_title}' deleted successfully!", "הודעת ההצלחה אינה תואמת את הציפיות."


def test_delete_user_not_found():
    """
    בדיקה שלילית: וידוא שכתובת ה-DELETE מחזירה שגיאה כאשר שם המשתמש לא קיים.
    """
    username_to_delete = "nonexistentuser"  # שם משתמש שאינו קיים במסד הנתונים
    delete_url = f"{BASE_URL}/user_delete/{username_to_delete}"

    # קריאה ל-DELETE
    delete_response = requests.delete(delete_url)

    # בדיקת תגובת ה-DELETE
    assert delete_response.status_code == 404, f"צפינו לקבל שגיאה 404 על שם המשתמש {username_to_delete}, אך קיבלנו קוד אחר."
    data = delete_response.json()
    assert "error" in data, "צפינו להודעת שגיאה בתגובה."
    assert data["error"] == f"user '{username_to_delete}' not found.", "הודעת השגיאה אינה תואמת את הציפיות."
