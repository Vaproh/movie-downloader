import os

from imdb import Cinemagoer
from arguments.args import arguments, parser
from modules.download.yts import YTS_downloader

ia = Cinemagoer()

inp = input("Enter movie name: ")
items = ia.search_movie(inp)
no = 1
for i in items:
    print(no,i)
    no += 1

movie_id = int(input("Enter movie id: "))
movie = items[movie_id-1]

ID = "tt"
ID = ID + str(movie.movieID)

print(f"Movie id is: {ID}\n\n")

try:
    magnet_link = YTS_downloader().get_magnet_url(movieID=ID, is_imdb=True, quality="4k")
    print(magnet_link)
    os.startfile(magnet_link)
except Exception as e:
    print(e)


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
