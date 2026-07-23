import httpx as rq
#from concurrent.futures import ThreadPoolExecutor

def scan(website):
    record = []

    response = rq.get(f"https://{website}/3324234adscsd").text
    false_positive = len(response)

    with open("dir_scan/txt/endpoint.txt", "r") as file:
        endpoints = file.readlines()

    # endpoints = endpoints.strip()

    response = rq.get(f"https://{website}/{endpoints}")

    if len(response.text) != false_positive:
        record.append(f"[+]{response.status_code}{endpoints}")
    
    return record

def format_print():
    pass