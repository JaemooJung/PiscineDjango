#!/usr/bin/env python3

import sys
import json
import requests
import dewiki

def get_wikipedia_page(page: str):
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "parse",
        "page": page.replace(" ", "_"),
        "prop" : "wikitext",
        "format": "json",
        "redirects": "true"
    }

    try:
        response = requests.get(url=url, params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise err
    
    try:
        data = json.loads(response.text)
    except json.JSONDecodeError as err:
        raise err
    
    if data.get("error"):
        raise Exception(data["error"]["info"])
    
    return (dewiki.from_string(data["parse"]["wikitext"]["*"]))


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 request_wikipedia.py <page_name>")
        return
    
    try:
        page = get_wikipedia_page(sys.argv[1])
    except Exception as err:
        print(f'Error while get page: {err}')
        return
    
    try:
        with open(f'{sys.argv[1]}.wiki', 'w') as f:
            f.write(page)
    except Exception as err:
        print(f'Error while save page: {err}')
        return
    
if __name__ == "__main__":
    main()