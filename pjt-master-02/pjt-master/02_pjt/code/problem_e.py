import requests
from pprint import pprint


def credits(title):

    URL = f'https://api.themoviedb.org/3/search/movie'
    
    param= {
        'api_key' : '6a5ece7778e61cb35c55c953b8743b0d',
        'language' : 'ko-KR',
        'region' : 'KR',
        'query' : title,
        'page' : 1
    }
    
    r = requests.get(URL, params = param).json().get('results')

    if not r:
        return None

    else:
        ids = r[0]['id']

    credit_URL = f'https://api.themoviedb.org/3/movie/{ids}/credits'

    credit_URL_param = {
        'api_key' : '6a5ece7778e61cb35c55c953b8743b0d',
        'language' : 'ko-KR',
        'region' : 'KR',
    }

    credit_movie = requests.get(credit_URL, params = credit_URL_param).json()
    
    credit_movie_cast = credit_movie['cast']
    credit_movie_crew = credit_movie['crew']    

    cast_dic = {
        'cast' : [],
        'directing' : []
    }
    for cr in credit_movie_crew:
        if cr['department'] == 'Directing':
            cast_dic['directing'] += [cr['name']]

    for ca in credit_movie_cast:
        if ca['known_for_department'] == 'Acting':
            if ca['cast_id'] < 10:
                cast_dic['cast'] += [ca['name']]

    return cast_dic





# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
