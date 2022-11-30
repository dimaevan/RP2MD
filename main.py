import argparse

from html_parser import parse_and_save


def run():
    args = arg_parsing()
    link = str(args.link).lower()
    parse_and_save(link)


def arg_parsing() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Link from realPython.org")
    parser.add_argument("-l", dest='link', required=True)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    run()
