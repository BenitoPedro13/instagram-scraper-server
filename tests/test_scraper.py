import json
import unittest
from unittest.mock import patch, MagicMock
from src.scraper.user_scraper import scrape_user
from src.scraper.post_scraper import scrape_post

class TestInstagramScraper(unittest.TestCase):

    @patch("src.scraper.user_scraper.client.get")
    def test_scrape_user(self, mock_get):
        fake_response = MagicMock()
        fake_response.content = json.dumps({
            "data": {
                "user": {
                    "username": "test_user",
                    "full_name": "Test User"
                }
            }
        }).encode("utf-8")
        mock_get.return_value = fake_response

        username = "test_user"
        user_data = scrape_user(username)
        self.assertIn("username", user_data)
        self.assertEqual(user_data["username"], username)

    @patch("src.scraper.post_scraper.httpx.post")
    def test_scrape_post(self, mock_post):
        fake_response = MagicMock()
        fake_response.content = json.dumps({
            "data": {
                "shortcode": "test_post",
                "id": "123"
            }
        }).encode("utf-8")
        mock_post.return_value = fake_response

        post_url = "https://www.instagram.com/p/test_post/"
        post_data = scrape_post(post_url)
        self.assertIn("shortcode", post_data)
        self.assertEqual(post_data["shortcode"], "test_post")

if __name__ == '__main__':
    unittest.main()
