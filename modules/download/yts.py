from sqlalchemy.testing.engines import mock_engine

from custom_wrapper.yts_api import YTSAPI


class YTS_downloader:

    def __init__(self):
        self.yts = YTSAPI(verify_ssl=True)

    def get_magnet_url(self, movieID, is_imdb=True, quality="1080p"):
        movie_details = self.yts.movie_details(movie_id=movieID, imdb=is_imdb)
        print(movie_details)
        hashNumber = 1

        if quality != "1080p":
            if quality == "720p":
                hashNumber = 0
            elif quality == "4k" or quality == "2160p":
                hashNumber = 2
            else:
                raise Exception("Invalid quality. Only available qualities are 720p, 1080p, 2160p/4K")

        try:
            hash_id = movie_details['data']['movie']['torrents'][hashNumber]['hash']
        except IndexError:
            raise Exception("The movie is not available in the selected quality.")

        return self.yts.get_magnet_url(hash_id)
