from app import myapp


def test_hello():
    response = myapp.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'hello world'