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
    for a in soup.find_all("a", {"class": "small text-muted"}):
        a.decompose()
    text = soup.find('div', {"class": "article-body"})

    return str(text)


def save_file(text: str, filename: str) -> None:
    try:
        with open(filename+".md", "w") as file:
            file.write(text)
    except TypeError:
        print("Nothing found")


def rename_output_file(name: str) -> str:
    beauty_name = name.lower().replace("-", " ").replace("/", "").capitalize()
    return beauty_name


def parse_and_save(link: str) -> None:
    parsed_link = urlparse(link)
    netloc = parsed_link.netloc
    path = parsed_link.path
    filename = rename_output_file(path)

    if is_link_an_article(netloc, path):
        save_file(parse_main_text(open_link(link)), filename)

