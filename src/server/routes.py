from flask import jsonify
from scraper.user_scraper import scrape_user
from scraper.post_scraper import scrape_post
from utils.parser import parse_user, parse_post

def setup_routes(app):
    @app.route('/user/<username>')
    def get_user(username):
        try:
            user_data = scrape_user(username)
            parsed_data = parse_user(user_data)
            return jsonify(parsed_data)
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @app.route('/post/<shortcode>')
    def get_post(shortcode):
        try:
            post_data = scrape_post(shortcode)
            parsed_data = parse_post(post_data)
            return jsonify(parsed_data)
        except Exception as e:
            return jsonify({"error": str(e)}), 400