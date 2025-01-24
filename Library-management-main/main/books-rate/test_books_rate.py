import pytest
import requests

# כתובת הבסיס של השירות
BASE_URL = "http://localhost:5006"

def test_add_rating_success():
    """
    positive test: test adding a rating to a book
    """
    # הוספת דירוג
    url = f"{BASE_URL}/add-rating"
    payload = {
        "title": "Kobi The Great",
        "rating": 5
    }
    response = requests.post(url, json=payload)

    # בדיקת תגובת ה-API
    assert response.status_code == 200, "failed to add rating"
    assert "average_rating" in response.json(), "average_rating is missing from the response"


def test_add_rating_invalid_rating():
    """
    negative test: test adding a rating with invalid rating
    """
    url = f"{BASE_URL}/add-rating"
    payload = {
        "title": "Nonexistent Book",
        "rating": 6 # invalid rating
    }
    response = requests.post(url, json=payload)

    assert response.status_code == 400, "expected status code 400"
    assert response.json()["error"] == "Rating must be an integer between 1 and 5"
