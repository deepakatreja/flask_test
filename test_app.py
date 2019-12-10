from p1 import myapp
import unittest

# python -m unittest test


class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = myapp.test_client()

    def test_main(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'
        #assert False

    def test_add(self):
        rv = self.app.get('/add/2/3')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, '5')

        rv = self.app.get('/add/0/10')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, '10')

    def test_404(self):
        rv = self.app.get('/other')
        self.assertEqual(rv.status, '404 NOT FOUND')

# from app import myapp


# def test_hello():
#     response = myapp.test_client().get('/')

#     assert response.status_code == 200
#     assert response.data == b'hello world'

# def test_deepak():
#     response = myapp.test_client().get('/deepak')

#     assert response.status_code == 200
#     assert response.data == b'hello deepak'

# def test_manish():
#     response = myapp.test_client().get('/manish')

#     assert response.status_code == 200
#     assert response.data == b'hello manish'

# def test_sahil():
#     response = myapp.test_client().get('/sahil')

#     assert response.status_code == 200
#     assert response.data == b'hello sahil'

