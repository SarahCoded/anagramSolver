import requests

response = requests.get('https://sarahcoded.pythonanywhere.com/')

def test_start():
    assert b'Live server testing is running'

def test_call_is_200():
    assert response.status_code == 200
