import requests
import pytest

@pytest.fixture(scope="module")
def placeholder_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response

def test_get_200_status_on_placeholder(placeholder_request):
    assert placeholder_request.status_code == 200, "wrong status code"

def test_response_json(placeholder_request):
    json = placeholder_request.json
    assert placeholder_request.status_code == 200, "wrong status code"