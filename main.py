import argparse
from urllib.parse import urlparse


def run():
    args = arg_parsing()
    link = str(args.link).lower()
    print(is_link_an_article(link))


def is_link_an_article(link: str):
    link = urlparse(link)
    netloc = link.netloc
    path = link.path
    if (netloc == "realpython.com") and path:
        return True
    return False


def arg_parsing() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Link from realPython.org")
    parser.add_argument("-l", dest='link', required=True)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    run()
