import json


def dec_movies(movies):
    movie_list = []
    for ids in movies:
        movie_id = ids['id']
        movie = json.load(open(f'data/movies/{movie_id}.json', encoding='utf-8'))
        movie_title = movie['title']
        movie_date = movie['release_date']
        if movie_date[5:7] == '12':
            movie_list.append(movie_title)
    return movie_list



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
