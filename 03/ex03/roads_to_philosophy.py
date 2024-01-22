import sys
import requests
from bs4 import BeautifulSoup

def get_first_valid_link(soup):
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for p in content_div.find_all("p", recursive=False):
        links = p.find_all("a", recursive=False)
        for link in links:
            href = link.get('href')
            if href and href.startswith("/wiki/") and not ':' in href:
                return href
    return None

def roads_to_philosophy(path):
    base_url = 'https://en.wikipedia.org'
    visited_titles = []
    count = 0

    while True:
        url = base_url + '/wiki/' + path
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find(id="firstHeading").text

        if title in visited_titles:
            print('It leads to an infinite loop!')
            break

        visited_titles.append(title)

        print(title)
        count += 1

        if 'Philosophy' in title:
            print(f'{count} roads from {visited_titles[0]} to philosophy.')
            break

        next_link = get_first_valid_link(soup)
        if next_link is None:
            print('It leads to a dead end!')
            break

        path = next_link.split('/')[-1]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python roads_to_philosophy.py [word]')
        sys.exit(1)

    roads_to_philosophy(sys.argv[1])
