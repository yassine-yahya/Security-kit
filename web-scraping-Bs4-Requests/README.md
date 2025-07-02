# web-scraing-Bs4-Requests
# Web Scraper and HTTP Security Header Checker

This Python script performs the following tasks:

- Scrapes a given URL.
- Checks for the presence of important HTTP security headers.
- Extracts the page's title and links.

## Features

- HTTP Security Header Check (e.g., `Strict-Transport-Security`, `X-Content-Type-Options`, etc.)
- Scrapes the webpage title and links.
- Colored output using `colorama` for better readability.

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `colorama`

## Installation


 Install the required libraries:
   - `pip install requests beautifulsoup4 colorama`

## Usage

1. Run the script:
   - `python scraper_and_security_checker.py`

2. When prompted, enter a URL (make sure to include `http://` or `https://`):
   - Example: `https://example.com`

3. The script will:
   - Check for the presence of key HTTP security headers.
   - Display the page title and any links on the page.

## Example Output

- The script will display a message with the status of security headers and output the title and links on the page.


