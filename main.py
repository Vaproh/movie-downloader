from search.search import MovieService

movies = MovieService().search_movies("The Matrix")

print(MovieService().get_movie_details(movies[0].movieID))

# def main():
#     print("Hello World")
#
# if __name__ == "__main__":
#     main()
