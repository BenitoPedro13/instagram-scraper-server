# README.md

# Instagram Scraper Server

This project implements a small server for an Instagram scraper that allows dynamic username input. It provides an API to scrape user and post data from Instagram.

## Project Structure

```
instagram-scraper-server
├── src
│   ├── scraper
│   │   ├── __init__.py
│   │   ├── user_scraper.py
│   │   └── post_scraper.py
│   ├── server
│   │   ├── __init__.py
│   │   ├── app.py
│   │   └── routes.py
│   └── utils
│       ├── __init__.py
│       └── parser.py
├── tests
│   ├── __init__.py
│   ├── test_scraper.py
│   └── test_server.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd instagram-scraper-server
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the server:
   ```
   python3 src/server/app.py
   ```

## Usage

- To scrape user data, send a GET request to `/user/<username>`.
- To scrape post data, send a GET request to `/post/<post_url>`.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.