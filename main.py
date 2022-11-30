import argparse


def run():
    arg_parsing()


def arg_parsing():
    parser = argparse.ArgumentParser(description="Link from realPython.org")
    parser.add_argument("-l", dest='link', required=True)


if __name__ == "__main__":
    run()
