import argparse

from arguments.download import add_download_args, download
from arguments.search import add_search_args, search

parser = argparse.ArgumentParser(description="A tool to download movies from various providers.")
subparsers = parser.add_subparsers(dest="command", help="Available commands")
search_parser = subparsers.add_parser("search", help="To search movies.")
download_parser = subparsers.add_parser("download", help="To download movies.")


def arguments():
    # Search subcommand
    add_search_args(search_parser)
    search_parser.set_defaults(func=search)

    # Download subcommand
    add_download_args(download_parser)
    download_parser.set_defaults(func=download)

    # Parse the arguments
    args = parser.parse_args()

    return args
