from search.search import MovieService
from arguments.args import arguments, parser

movies = MovieService().search_movies("The Matrix")

print(MovieService().get_movie_details(movies[0].movieID))

def main():
    args = arguments()

    # Call the appropriate function based on the subcommand
    if hasattr(args, "func"):
        if args.verbose:
            print("Verbose mode enabled")
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
