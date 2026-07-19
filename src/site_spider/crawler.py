import sys
import requests as rq
from concurrent.futures import ThreadPoolExecutor

if len(sys.argv) != 2:
    sys.exit("Usage: python crawler.py <website>")

website = sys.argv[1]

response = rq.get(f"https://{website}/3324234adscsd").text
false_positive = len(response)


def scan(endpoint):
    endpoint = endpoint.strip()

    response = rq.get(f"https://{website}/{endpoint}")

    if len(response.text) != false_positive:
        print(endpoint, response.status_code)


with open("txt/endpoint.txt", "r") as file:
    endpoints = file.readlines()

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan, endpoints)