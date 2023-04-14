import json
from pprint import pprint

# id,title,poster_path,vote_average,overview,genre_names

def movie_info(movie, genres):
    name_list = []
    for j in range(len(movie['genre_ids'])):
        for i in genres:
            if i['id'] == movie['genre_ids'][j]:
                name_list.append(i['name'])
    result = {
        'id' : movie['id'],
        'title' : movie['title'],
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_names' : name_list
    }
    return result
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
