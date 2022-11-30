from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse


def is_link_an_article(netloc: str, path: str):
    if (netloc == "realpython.com") and path:
        return True
    return False


def open_link(link: str) -> str:
    request_object = requests.get(link)
    return request_object.text if request_object.status_code == 200 else print("Bad links")


def parse_main_text(html: str):
    soup = BeautifulSoup(html, 'lxml')
    text = soup.find('div', {"class": "article-body"})
    return str(text)


def save_file(text: str) -> None:
    try:
        with open("output.md", "w") as file:
            file.write(text)
    except TypeError:
        print("Nothing found")


def parse_and_save(link: str) -> None:
    parsed_link = urlparse(link)
    netloc = parsed_link.netloc
    path = parsed_link.path

    if is_link_an_article(netloc, path):
        save_file(parse_main_text(open_link(link)))

