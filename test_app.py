import pytest
import requests

def test_predict():
    url = "http://127.0.0.1:5000/predict"
    params = {'x': 3, 'y': 4}

    response = requests.get(url, params=params)

    assert response.status_code == 200

    data = response.json()
    assert data["features"]["x"] == 3
    assert data["features"]["y"] == 4
    assert data["prediction"] == 1


