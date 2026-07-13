# Site Spider

Site Spider is a simple Python tool for directory discovery and web scraping. It can scan a website using a wordlist to discover common directories and files, and it can also scrape data from supported websites.

I built this project to better understand how web requests work, how command-line tools accept user input, and how tools like Gobuster perform basic directory enumeration. It also gave me hands-on experience with web scraping and working with HTTP responses.

## What I Learned

While building this project, I learned how to work with the `requests` library, read files line by line, accept command-line arguments using `sys.argv`, build a simple command-line application, understand HTTP status codes, and organize a Python project into reusable components.

## Usage

Install the required dependency:

```bash
pip install requests
```

Run the program:

```bash
python spider.py example.com
```

The program reads endpoints from `endpoint.txt`, sends a request to each one, and displays the HTTP status code for every response. It also includes website-specific scraping features for supported websites.

## Note

This project was created for educational purposes to practice Python and understand the basics of web scraping and directory enumeration. Only scan or scrape websites that you own or have permission to test.
