import requests


def popular_count():
    movie_code = 'popular'

    URL = f'https://api.themoviedb.org/3/movie/{movie_code}'

    param= {
    'api_key' : '6a5ece7778e61cb35c55c953b8743b0d',
    'language' : 'ko-KR',
    'region' : 'KR'
    }

    r = requests.get(URL, params = param).json()

    return len(r['results'])

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
