import requests
from bs4 import BeautifulSoup as bs
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import urllib.request
from io import BytesIO

my_api_key = "6a5ece7778e61cb35c55c953b8743b0d"

movies, english_movies = [], []
for idx in range(1, 501):
    # Data 정리하기
    popular_movie_url = 'https://api.themoviedb.org/3/movie/popular?api_key=' + my_api_key + '&language=ko-kr&page=' + str(idx)

    res = requests.get(popular_movie_url).text
    data = json.loads(res)
    movies += data['results']
    
# (-----------------------------------------------------------------------------)

    english_movie_url = 'https://api.themoviedb.org/3/movie/popular?api_key=' + my_api_key + '&language=en-US&page=' + str(idx)

    english_res = requests.get(english_movie_url).text
    english_data = json.loads(english_res)
    english_movies += english_data['results']
    
features_name = list(movies[0].keys())

df_movies = pd.DataFrame(movies, columns= features_name)

english_features_name = list(english_movies[0].keys())

df_english_movies = pd.DataFrame(english_movies, columns= english_features_name)

df_movies['eng_title'] = df_english_movies['title']
df_movies = df_movies.drop(columns=['original_title'])

# 장르 가져오기 https://api.themoviedb.org/3/genre/movie/list?api_key=<<api_key>>
genre_url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=' + my_api_key
genre_res = requests.get(genre_url).text
genre_list = json.loads(genre_res)['genres']
df_genres = pd.DataFrame(genre_list, columns=['id', 'name'])

    
genre_names = []
for idx in range(len(df_movies)):
    movie = df_movies.iloc[idx]
    change_list = []
    for gen in movie['genre_ids']:
        change_list.append(list(df_genres['name'][df_genres['id'] == gen])[0])
    genre_names.append(change_list)
df_movies['genre_ids'] = genre_names

total_yt_url_list = []

for movie_idx in range(len(df_movies)):
    movie_id = df_movies.iloc[movie_idx]['id']
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
df_movies['video'] = total_yt_url_list

# 1:N table을 위한 id, video에 대한 df를 생성
df_all_video = df_movies[['id','video']]
df_all_video = df_all_video.explode("video", ignore_index=True)
df_all_video.rename(columns = {'id' : 'movie_id'}, inplace = True)

# 1:N table을 위한 movie_id, genre_ids에 대한 df를 생성
df_all_genres = df_movies[['movie_id','genre_ids']]
df_all_genres = df_all_genres.explode("genre_ids", ignore_index=True)
df_movies = df_movies.drop(columns = ['genre_ids'])

# video를 지우고 column명을 id에서 movie_id로 변환
df_movies = df_movies.drop(columns = ['video'])
df_movies.rename(columns = {'id' : 'movie_id'}, inplace = True)


df_movies.to_json(r'./movies/fixtures/all_movie.json', force_ascii=False, orient = 'records', indent=4)
df_all_video.to_json(r'./movies/fixtures/all_movie_video.json', force_ascii=False, orient = 'records', indent=4)
df_all_genres.to_json(r'./movies/fixtures/all_movie_genre.json', force_ascii=False, orient = 'records', indent=4)

# 데이터 형태 바꾸기 (django model에 추가하기 위한 과정)

with open('./movies/fixtures/all_movie.json') as f:
    all_movie_js = json.loads(f.read()) ## json 라이브러리 이용

with open('./movies/fixtures/all_movie_video.json') as f:
    all_video_js = json.loads(f.read()) ## json 라이브러리 이용

with open('./movies/fixtures/all_movie_genre.json') as f:
    all_genre_js = json.loads(f.read()) ## json 라이브러리 이용

all_movie_list = list(all_movie_js)
all_video_list = list(all_video_js)
all_genre_list = list(all_genre_js)

for movie in all_movie_list:
    if movie['backdrop_path']:
        movie['backdrop_path'] = 'https://image.tmdb.org/t/p/original' + movie['backdrop_path']
    if movie['poster_path']:
        movie['poster_path'] = 'https://image.tmdb.org/t/p/original' + movie['poster_path']

new_all_movie_list, new_all_video_list, new_all_genre_list = [], [], []
for movie in all_movie_list:
    # Movie 모델 필드명에 맞추어 데이터를 저장함.
    data = {
        "model": "movies.AllMovie",
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
    new_all_movie_list.append(data)
    
for video in all_video_list:
    # Movie 모델 필드명에 맞추어 데이터를 저장함.
    data = {
        "model": "movies.AllRelatedVideo",
        'fields': {
            "movie_id" : video['movie_id'],
            "video" : video['video']
        },
    }
    new_all_video_list.append(data)

for genre in all_genre_list:
    # Movie 모델 필드명에 맞추어 데이터를 저장함.
    data = {
        "model": "movies.AllGenre",
        'fields': {
            "movie_id" : genre['movie_id'],
            "genre_ids" : genre['genre_ids']
        },
    }
    new_all_genre_list.append(data)

with open('./movies/fixtures/all_movie.json','w') as f:
    json.dump(new_all_movie_list,f, ensure_ascii=False, indent=4)
with open('./movies/fixtures/all_movie_video.json','w') as f:
    json.dump(new_all_video_list,f, ensure_ascii=False, indent=4)
with open('./movies/fixtures/all_movie_genre.json','w') as f:
    json.dump(new_all_genre_list,f, ensure_ascii=False, indent=4)