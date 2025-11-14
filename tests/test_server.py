import unittest
from unittest.mock import patch
from src.server.app import create_app

class TestServer(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    @patch("src.utils.parser.parse_user", return_value={"username": "google"})
    @patch("src.scraper.user_scraper.scrape_user", return_value={"username": "google"})
    def test_get_user_data(self, mock_scrape_user, mock_parse_user):
        response = self.app.get('/user/google')  # Example username
        self.assertEqual(response.status_code, 200)
        self.assertIn('username', response.get_json())

if __name__ == '__main__':
    unittest.main()
