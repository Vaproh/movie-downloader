from imdb import Cinemagoer  # For accessing IMDb


class MovieService:
    def __init__(self):
        """
        Initialize the MovieService with IMDb and YTS API base URL.
        """
        self.ia = Cinemagoer()

    def search_movies(self, movie_title):
        """
        Searches for movies based on a provided movie title using IMDb's resources and
        returns the list of found movies. If an error occurs during the process, a
        message is printed, and an empty list is returned.

        :param movie_title: A string representing the title or part of the title of the movie.
        :type movie_title: str
        :return: A list of movies matching the provided title. Returns an empty list
            if an exception occurs during the search.
        :rtype: list
        :raises Exception: Any exception encountered while attempting to search for movies.
        """
        try:
            movies = self.ia.search_movie(movie_title)
            return movies
        except Exception as e:
            print(f"An error occurred while searching for movies: {e}")
            return []

    def get_movie_details(self, imdb_id):
        """
        Fetch detailed information about a specific movie by IMDb ID using IMDbPY.

        :param imdb_id: IMDb ID of the movie (e.g., "tt0111161").
        :return: A dictionary with detailed movie information.
        """
        try:
            # Fetch movie details using IMDbPY
            movie = self.ia.get_movie(imdb_id.lstrip('tt'))
            return {
                'title': movie.get('title', 'Unknown Title'),
                'year': movie.get('year', 'Unknown Year'),
                'genres': movie.get('genres', []),
                'rating': movie.get('rating', 'N/A'),
                'directors': [director.get('name') for director in movie.get('directors', [])],
                'cast': [cast_member.get('name') for cast_member in movie.get('cast', [])[:10]],  # Top 10 cast members
                'plot': movie.get('plot outline', 'No Plot Available')
            }
        except Exception as e:
            print(f"Error fetching IMDb details: {e}")
            return {}
