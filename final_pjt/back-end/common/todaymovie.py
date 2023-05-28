def get_today_movie_list():
    import requests
    from bs4 import BeautifulSoup as bs
    import json
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from datetime import date, datetime, timedelta

    
    # 오늘 날짜 자동 계산
    ymd = date.today() - timedelta(1)
    ymd = datetime.strftime(ymd, '%Y%m%d')
    # print(ymd)

    # 오늘 상영중인 영화
    my_api_key = "6a5ece7778e61cb35c55c953b8743b0d"
    today_movie_key = "0163c18e093080d6b1ad11fa2fadfad1"

    today = ymd

    today_movie_url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=' + today_movie_key + '&targetDt=' + today
    today_movie_res = requests.get(today_movie_url).text
    today_movie_data = json.loads(today_movie_res)
    today_movies = today_movie_data['boxOfficeResult']['dailyBoxOfficeList']

    # 하루에 한번
    # 오늘의 영화 제목을 활용하여 movie detail을 불러오기
    today_movie_detail_list = []
    english_movies = []
    for movie in today_movies:
        movie_name = movie['movieNm']
        search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key=' + my_api_key + '&query=' + movie_name + '&include_adult=false&language=ko-KR&page=1'

        search_movie_res = requests.get(search_movie_url).text
        search_movie_data = json.loads(search_movie_res)
        print(search_movie_data['results'])
        print('check -----------------------------------------')
        if search_movie_data['results']:
            search_movie = search_movie_data['results'][0]
        else:
            continue
        
        today_movie_detail_list.append(search_movie)
    
        english_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key=' + my_api_key + '&query=' + movie_name + '&include_adult=false&language=en-US&page=1'

        english_res = requests.get(english_movie_url).text
        english_data = json.loads(english_res)
        english_movies += english_data['results']

    df_today_movies = pd.DataFrame(today_movie_detail_list, columns = today_movie_detail_list[0].keys())

    english_features_name = list(english_movies[0].keys())

    df_english_movies = pd.DataFrame(english_movies, columns= english_features_name)

    df_today_movies['eng_title'] = df_english_movies['title']
    df_today_movies = df_today_movies.drop(columns=['original_title'])

    # 장르 변환
    genre_url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=' + my_api_key
    genre_res = requests.get(genre_url).text
    genre_list = json.loads(genre_res)['genres']
    df_genres = pd.DataFrame(genre_list, columns=['id', 'name'])


    today_genre_names = []
    for idx in range(len(df_today_movies)):
        today_movie = df_today_movies.iloc[idx]
        change_list = []
        for gen in today_movie['genre_ids']:
            change_list.append(list(df_genres['name'][df_genres['id'] == gen])[0])
        today_genre_names.append(change_list)
    df_today_movies['genre_ids'] = today_genre_names

    # poster_path
    image_url_list = []
    for idx in range(len(df_today_movies)):
        today_movie = df_today_movies.iloc[idx]
        image_url = 'https://image.tmdb.org/t/p/original' + df_today_movies.iloc[idx]['poster_path']
        image_url_list.append(image_url)
    
    df_today_movies['poster_path'] = image_url_list
    
        
    # df_today_movies = df_today_movies.drop(columns = ['video'])

    # 유튜브 video url
    # 'https://www.youtube.com/watch?v=' + video에 있는 key

    # 연관 video url

    total_yt_url_list = []

    for today_movie_idx in range(len(df_today_movies)):
        movie_id = df_today_movies.iloc[today_movie_idx]['id']
        movie_id = str(movie_id)
        video_url = 'https://api.themoviedb.org/3/movie/' + movie_id + '/videos?api_key=' + my_api_key +'&language=en-US'
        video_res = requests.get(video_url).text
        video_data = json.loads(video_res)
        video_data = video_data['results'][:5]

        yt_url_list = []

        for video_key in video_data:
            video_key = video_key['key']
            yt_url = 'https://www.youtube.com/watch?v=' + video_key
            yt_url_list.append(yt_url)
        total_yt_url_list.append(yt_url_list)
    df_today_movies['video'] = total_yt_url_list
    
    # 1:N을 위한 video 따로 저장
    df_today_video = df_today_movies[['id','video']]
    df_today_video = df_today_video.explode("video", ignore_index=True)
    df_today_video.rename(columns = {'id' : 'movie_id'}, inplace = True)
    
    # video column을 삭제하고 id column을 movie_id로 변환
    df_today_movies = df_today_movies.drop(columns = ['video'])
    df_today_movies.rename(columns = {'id' : 'movie_id'}, inplace = True)
    
    # 1:N table을 위한 movie_id, genre_ids에 대한 df를 생성
    df_today_genres = df_today_movies[['movie_id','genre_ids']]
    df_today_genres = df_today_genres.explode("genre_ids", ignore_index=True)
    df_today_movies = df_today_movies.drop(columns = ['genre_ids'])
    
    print(df_today_movies)
    print('check directory')
    df_today_movies.to_json(r'./movies/fixtures/{}_movie.json'.format(today), force_ascii=False, orient = 'records', indent=4)
    df_today_video.to_json(r'./movies/fixtures/{}_video.json'.format(today), force_ascii=False, orient = 'records', indent=4)
    df_today_genres.to_json(r'./movies/fixtures/{}_genre.json'.format(today), force_ascii=False, orient = 'records', indent=4)
    
 
    with open('./movies/fixtures/{}_movie.json'.format(today), 'r', encoding='UTF-8') as f:
        today_movie_js = json.loads(f.read()) ## json 라이브러리 이용
        # today_movie_js = json.dumps(today_movie_js, ensure_ascii = False)

    with open('./movies/fixtures/{}_video.json'.format(today)) as f:
        today_video_js = json.loads(f.read()) ## json 라이브러리 이용

    with open('./movies/fixtures/{}_genre.json'.format(today)) as f:
        today_genre_js = json.loads(f.read()) ## json 라이브러리 이용

    today_movie_list = today_movie_js
    today_video_list = list(today_video_js)
    today_genre_list = list(today_genre_js)

    for movie in today_movie_list:
        if movie['backdrop_path']:
            movie['backdrop_path'] = 'https://image.tmdb.org/t/p/original' + movie['backdrop_path']
    
    new_today_movie_list, new_today_video_list, new_today_genre_list = [], [], []
    
    for movie in today_movie_list:
        # Movie 모델 필드명에 맞추어 데이터를 저장함.
        data = {
            "model": "movies.TodayMovie",
            'fields': {
                "adult": movie['adult'],
                "backdrop_path": movie['backdrop_path'],
                "movie_id": movie['movie_id'],
                "original_language": movie['original_language'],
                "overview": movie['overview'],
                "popularity": movie['popularity'],
                "poster_path": movie['poster_path'],
                "release_date": movie['release_date'],
                "title": movie['title'],
                "vote_average": movie['vote_average'],
                "vote_count": movie['vote_count'],
                "eng_title": movie['eng_title']
            },
        }
        new_today_movie_list.append(data)
        
    for video in today_video_list:
        # Movie 모델 필드명에 맞추어 데이터를 저장함.
        data = {
            "model": "movies.TodayRelatedVideo",
            'fields': {
                "movie_id" : video['movie_id'],
                "video" : video['video']
            },
        }
        new_today_video_list.append(data)

    for genre in today_genre_list:
        # Movie 모델 필드명에 맞추어 데이터를 저장함.
        data = {
            "model": "movies.TodayGenre",
            'fields': {
                "movie_id" : genre['movie_id'],
                "genre_ids" : genre['genre_ids']
            },
        }
        new_today_genre_list.append(data)
    
    with open('./movies/fixtures/{}_movie.json'.format(today),'w', encoding='UTF-8') as f:
        json.dump(new_today_movie_list, f, ensure_ascii=False, indent=4)
    with open('./movies/fixtures/{}_video.json'.format(today),'w', encoding='UTF-8') as f:
        json.dump(new_today_video_list, f, ensure_ascii=False, indent=4)
    with open('./movies/fixtures/{}_genre.json'.format(today),'w', encoding='UTF-8') as f:
        json.dump(new_today_genre_list, f, ensure_ascii=False, indent=4)
    
    
    return df_today_movies