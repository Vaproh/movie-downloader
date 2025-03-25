from modules.search import MovieService
from arguments.args import arguments, parser

movies = MovieService().search_movies("The Matrix")

print(movies[0].movieID)

def main():
    print("\n")
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
