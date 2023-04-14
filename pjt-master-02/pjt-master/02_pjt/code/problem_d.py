import requests
from pprint import pprint


def recommendation(title):

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
    
    
    recom_URL = f'https://api.themoviedb.org/3/movie/{ids}/recommendations'

    recom_URL_param = {
        'api_key' : '6a5ece7778e61cb35c55c953b8743b0d',
        'language' : 'ko-KR',
        'region' : 'KR',
    }
    
    recom_movie = requests.get(recom_URL, params = recom_URL_param).json().get('results')


    if not recom_movie :
        return []

    else:
        return recom_movie




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
