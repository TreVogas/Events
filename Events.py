import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, urljoin
import urllib3
import numpy as np
import json

base_url = "https://it-events.com/"

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/88.0.4324.190 Safari/537.36', 'accept': '*/*'}
urllib3.disable_warnings()


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params, verify=False)  # proxies=proxy
    return r


def get_links(html):  # get links on the vacancy
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', class_='event-list-item__title')
    all_links = []
    for link in links:
        all_links.append('https://it-events.com/' + link.get('href'))
    return all_links


def get_pages_link(html, url_list=[]):  # get the number of pages, which will be scraping
    soup = BeautifulSoup(html, 'html.parser')
    count_page = soup.find_all('a', class_='paging__item')
    for page in count_page:
        if page.text == 'Следующая':
            url = base_url + page.get('href')
            url_list.append(url)
            get_pages_link(get_html(url).content)
            return url_list


def get_pages_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    event_name = soup.find('h1', class_='event-header__title').text
    return event_name


html = get_html(base_url)
paper = get_pages_link(html.content)
paper.insert(0, base_url)
events = np.array([])
for link in paper:
    html = get_html(link)
    events = np.append(events, get_links(html.content))

info = []
for event in events:
    html = get_html(event).content
    soup = BeautifulSoup(html, 'html.parser')
    event_info = []
    event_info.append(get_pages_info(html))
    info.append(event_info)
print(info)