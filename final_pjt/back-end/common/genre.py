import requests
import json

my_api_key = "6a5ece7778e61cb35c55c953b8743b0d"
genre_url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=' + my_api_key
genre_res = requests.get(genre_url).text
genre_list = json.loads(genre_res)['genres']
print(genre_list)
for genre_set in genre_list:
    print(genre_set['name'])