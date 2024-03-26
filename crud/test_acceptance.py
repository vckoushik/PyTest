import pytest
import requests

ENDPOINT= "http://127.0.0.1:8000/"

def test_concurrent_requests():
    # Simulate concurrent requests to the API
    for i in range(10):
        response = requests.get(ENDPOINT)
        assert response.status_code == 200

def test_error_handling():
    # Simulate error handling on the API
    response = requests.get(ENDPOINT+"/invalid_url")
    assert response.status_code == 404