import requests as rq
from bs4 import BeautifulSoup as bs


def send_req(url):
    data = rq.get(f"https://{url}")
    return data.status_code

# def website_req():
#     data = rq.get("https://books.toscrape.com").text
#     return data

# def get_data():
#     data = website_req()
#     soup = bs(data, 'html.parser')
#     tag = soup.ol.find_all('h3').get_text()
#     return tag

# def praser():
#     raw_data = get_data()
#     # text = "".join(raw_data)
#     # replacements = {"</h3>": "", "<h3>": "", "</a>": ""}
#     # for old, new in replacements.items():
#     #     text = text.replace(old, new)
#     return raw_data

# def main():
#     books_names = praser()
#     print(books_names)


