import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_page(url, folder):
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join(folder, urlparse(url).path.replace('/', '_') + '.html')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        return response.text
    return None

def scrape_links(url, folder, visited):
    if url in visited:
        return
    visited.add(url)
    html = download_page(url, folder)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a', href=True):
            absolute_link = urljoin(url, link['href'])
            if urlparse(absolute_link).netloc == urlparse(url).netloc:
                scrape_links(absolute_link, folder, visited)

def main(start_url):
    folder = 'downloaded_pages'
    os.makedirs(folder, exist_ok=True)
    visited = set()
    scrape_links(start_url, folder, visited)

if __name__ == '__main__':
    main('https://networklessons.com/cisco/ccna-200-301')  # Замените на нужный URL