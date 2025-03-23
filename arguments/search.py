import argparse


def add_search_args(parser: argparse.ArgumentParser):
    # IMDb ID
    parser.add_argument(
        "--imdb-id",
        type=str,
        help="The IMDb ID of the movie (e.g., 'tt1375666')."
    )

    # Provider movie ID
    parser.add_argument(
        "--movieid",
        type=str,
        help="The movie ID specific to the provider (e.g., YTS movie ID)."
    )

    # Provider
    parser.add_argument(
        "--provider",
        type=str,
        default="YTS",
        help="The movie provider or service to search from (default: 'YTS')."
    )

    # Movie Name
    parser.add_argument(
        "--movie-name",
        type=str,
        help="The name of the movie to search for."
    )

    # List flag
    parser.add_argument(
        "--list",
        action="store_true",  # This creates a flag
        help="Return a list of movies instead of a specific movie."
    )

    # FZF flag
    parser.add_argument(
        "--fzf",
        action="store_true",  # This creates a flag
        help="Use fzf fuzzy finder for movie selection."
    )


def search(args):
    """Logic for the search subcommand."""
    pass
