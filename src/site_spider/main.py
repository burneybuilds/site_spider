import sys
import argparse

from scraper import send_req

def print_options():
    options = ["[+] Img to Loc ",
                "[+] Crawler",
                "[+] WebScrapper"]
    for op in options:
        print(op)

def cli_mode():
    print_options()


def main():

    parser = argparse.ArgumentParser(description="List of Commands.",  usage="%(prog)s --find <url> | --img2loc <image> | --cli | --scrape <url>")

    parser.add_argument("-f", "--find", help="URL to scan.")
    parser.add_argument("-i", "-img2loc", help="Check for Gps in a photo.", )
    parser.add_argument("-c", "--cli", help="Open cli mode.", )
    parser.add_argument("-s", "--scarap", help="Scrap data from the list of websites.") 

    args = parser.parse_args()

    # Finds end points.
    if args.find:
        code = send_req(args.find)
        print(code)

    # Scraps data from websites.
    if args.scarap:
        print(f"Crawling:")
    
    # Truns one the cli mode.
    if args.cli:
        pass

    # Finds Gps data from an img.
    if args.img2loc:
        print(f"Finding location for:")
    
    

if __name__ == "__main__":
    main()