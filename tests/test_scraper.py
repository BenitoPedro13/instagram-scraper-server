import unittest
from src.scraper.user_scraper import scrape_user
from src.scraper.post_scraper import scrape_post

class TestInstagramScraper(unittest.TestCase):

    def test_scrape_user(self):
        username = "test_user"
        user_data = scrape_user(username)
        self.assertIn("username", user_data)
        self.assertEqual(user_data["username"], username)

    def test_scrape_post(self):
        post_url = "https://www.instagram.com/p/test_post/"
        post_data = scrape_post(post_url)
        self.assertIn("shortcode", post_data)
        self.assertEqual(post_data["shortcode"], "test_post")

if __name__ == '__main__':
    unittest.main()