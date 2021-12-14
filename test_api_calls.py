import requests

def test_start():
    assert b'API call testing is running'

response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/test")
response_body = response.json()

def test_call_is_200():
    assert response.status_code == 200

def test_JSON_format():
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

def test_correct_word():
    assert response_body[0]["word"] == "test"

def test_correct_definition():
    assert response_body[0]["meanings"][0]["definitions"][0]["definition"] == "a procedure intended to establish the quality, performance, or reliability of something, especially before it is taken into widespread use."
    