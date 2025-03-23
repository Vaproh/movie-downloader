import argparse


def add_download_args(parser: argparse.ArgumentParser):
    # Save torrent file
    parser.add_argument(
        "--save-torrent",
        action="store_true",
        help="Save the torrent file to output directory."
    )

    # Quality to save
    parser.add_argument(
        "--quality",
        type=str,
        help="The quality to save (e.g., '720p'). Available qualities ('480p', '720p', '1080p', '4k')."
    )

    # Generate a magnet url
    parser.add_argument(
        "--magnet",
        action="store_true",
        help="Generate a magnet URL instead of torrent file."
    )

    # Open directly in torrent.
    parser.add_argument(
        "--open",
        action="store_true",
        help="Open the torrent file directly in torrent client."
    )

def download(args):
    """Logic for the download subcommand."""
    pass
