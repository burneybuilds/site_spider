import sys
import requests as rq


website = sys.argv[1]

if website != True:
    sys.exit("Useage: Python crawler.py <website> || Py crawler.py <website")

with open("endpoint.txt", "r") as files:
    for endpoint in files:
        endpoint = endpoint.strip()
        response = rq.get(f"https://{website}/{endpoint}")
        print(endpoint , response.status_code)