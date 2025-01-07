import unittest
from src.server.app import app

class TestServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_user_data(self):
        response = self.app.get('/user/google')  # Example username
        self.assertEqual(response.status_code, 200)
        self.assertIn('username', response.get_json())

if __name__ == '__main__':
    unittest.main()