from lib.yts_api import YTSAPI
from lib.imdb_helper import IMDbHelper
import imdb
import certifi

imdb = imdb.IMDb()
imdb_help = IMDbHelper()
yts = YTSAPI(verify_ssl=True, custom_ca_bundle=certifi.where())

k = input("Enter a movie name: ")

items = imdb.get_imdbID()
for i in items:
    print(i)
