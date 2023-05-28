from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.db import connections
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import AllMovieListSerializer, AllVideoListSerializer, AllGenreSerializer, CommentSerializer
from .serializers import TodayMovieListSerializer, TodayVideoListSerializer, TodayGenreSerializer
from .serializers import MovieDetailSerializer, ActorListSerializer, MovieSerializer
from .models import AllGenre, TodayGenre, AllMovie, AllRelatedVideo, TodayMovie, TodayRelatedVideo, Comment, TodayMovieCreated, MovieDetail
from .models import MovieDetail, ActorList

from common.todaymovie import get_today_movie_list
from common.detail import movie_detail_url
from common.profilecosine import profileprocess
from datetime import date, datetime, timedelta
import json
import requests
import pandas as pd
from common.cosine import preprocess
from django.conf import settings

from django.contrib.auth import get_user_model

def exchange_secret_key():
    EXCHANGE_SECRET_KEY = getattr(settings, 'EXCHANGE_SECRET_KEY', 'EXCHANGE_SECRET_KEY')
    return EXCHANGE_SECRET_KEY


def delete_yesterday():
    movie_list = TodayMovie.objects.all()
    for movie in movie_list:
        movie.delete()
    video_list = TodayRelatedVideo.objects.all()
    for video in video_list:
        video.delete()
    genre_list = TodayGenre.objects.all()
    for genre in genre_list:
        genre.delete()

def today_json_to_db():
    ymd = date.today() - timedelta(1)
    ymd = datetime.strftime(ymd, '%Y%m%d')
    today = ymd
    with open('./movies/fixtures/{}_movie.json'.format(today), 'r', encoding='UTF-8') as f:
        today_movie_js = json.loads(f.read()) ## json 라이브러리 이용

    with open('./movies/fixtures/{}_video.json'.format(today)) as f:
        today_video_js = json.loads(f.read()) ## json 라이브러리 이용

    with open('./movies/fixtures/{}_genre.json'.format(today)) as f:
        today_genre_js = json.loads(f.read()) ## json 라이브러리 이용

    today_movie_list = today_movie_js
    today_video_list = list(today_video_js)
    today_genre_list = list(today_genre_js)
    
    for movie in today_movie_list:
        # Movie 모델 필드명에 맞추어 데이터를 저장함.
        movie_list = TodayMovie()
        movie = movie['fields']
        movie_list.adult = movie['adult']
        movie_list.backdrop_path = movie['backdrop_path']
        movie_list.movie_id = movie['movie_id']
        movie_list.original_language = movie['original_language']
        movie_list.overview = movie['overview']
        movie_list.popularity = movie['popularity']
        movie_list.poster_path = movie['poster_path']
        movie_list.release_date = movie['release_date']
        movie_list.title = movie['title']
        movie_list.vote_average = movie['vote_average']
        movie_list.vote_count = movie['vote_count']
        movie_list.eng_title = movie['eng_title']
        movie_list.save()
    
    for videos in today_video_list:
        video_list = TodayRelatedVideo()
        videos = videos['fields']
        video_list.movie_id = videos['movie_id']
        video_list.video = videos['video']
        video_list.save()
        
    for genres in today_genre_list:
        genre_list = TodayGenre()
        genres = genres['fields']
        genre_list.movie_id = genres['movie_id']
        genre_list.genre_ids = genres['genre_ids']
        genre_list.save()
    
# @api_view(['GET', 'POST'])
# # @permission_classes([IsAuthenticated])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = get_list_or_404(AllMovie)
#         serializer = AllMovieListSerializer(movies, many=True)
#         for iidx in range(len(serializer.data)):
#             genre_list, video_list = [], []
#             for genre in dict(serializer.data[iidx])['genres']:
#                 genre_list.append(dict(genre)['genre_ids'])
#             for idx, i in enumerate(genre_list):
#                 serializer.data[iidx]['genres'][idx] = i
                
#             for video in dict(serializer.data[iidx])['videos']:
#                 video_list.append(dict(video))
#             for v_idx, v in enumerate(video_list):
#                 serializer.data[iidx]['videos'][v_idx] = v['video']
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = AllMovieListSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             # serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

def make_df(li):
    df = pd.DataFrame(data=li, columns=li[0].keys())
    return df


@api_view(['GET'])
def best_movie_list(request):
    movies = AllMovie.objects.all()
    movies = movies.order_by('-popularity')
    movies = movies[:10]
    serializer = AllMovieListSerializer(movies, many=True)
    for iidx in range(len(serializer.data)):
        genre_list, video_list = [], []
        for genre in dict(serializer.data[iidx])['genres']:
            genre_list.append(dict(genre)['genre_ids'])
        for idx, i in enumerate(genre_list):
            serializer.data[iidx]['genres'][idx] = i
            
        for video in dict(serializer.data[iidx])['videos']:
            video_list.append(dict(video))
        for v_idx, v in enumerate(video_list):
            serializer.data[iidx]['videos'][v_idx] = v['video']
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def today_movie_list(request):
    TodayMovieCreated.objects.today = datetime.now()
    ymd = date.today()
    today_ymd = datetime.strftime(ymd, '%Y-%m-%d')
    days, is_created = TodayMovieCreated.objects.get_or_create()
    print(days)
    if is_created:
        delete_time = TodayMovieCreated.objects.all()
        for x in delete_time:
            x.delete()
        days, is_created = TodayMovieCreated.objects.get_or_create()
        days.today = today_ymd
        get_today_movie_list()
        today_json_to_db()
    else:
        if not TodayMovie.objects.all():
            delete_yesterday()
            delete_time = TodayMovieCreated.objects.all()
            for x in delete_time:
                x.delete()
            days, is_created = TodayMovieCreated.objects.get_or_create()
            get_today_movie_list()
            today_json_to_db()
        elif today_ymd != str(days.today)[:10]:
            delete_yesterday()
            delete_time = TodayMovieCreated.objects.all()
            for x in delete_time:
                x.delete()
            days, is_created = TodayMovieCreated.objects.get_or_create()
            get_today_movie_list()
            today_json_to_db()
            
    if request.method == 'GET':
        movies = get_list_or_404(TodayMovie)
        serializer = TodayMovieListSerializer(movies, many=True)
        for iidx in range(len(serializer.data)):
            genre_list, video_list = [], []
            for genre in dict(serializer.data[iidx])['genre_ids']:
                genre_list.append(dict(genre)['genre_ids'])
            for idx, i in enumerate(genre_list):
                serializer.data[iidx]['genre_ids'][idx] = i
            
            for video in dict(serializer.data[iidx])['videos']:
                video_list.append(dict(video))
            for v_idx, v in enumerate(video_list):
                serializer.data[iidx]['videos'][v_idx] = v['video']
                
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodayMovieListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_page(request, page_id):
    for i in range(20):
        movies = AllMovie.objects.all()
        movies = movies[page_id*20-20 : page_id*20]
        # print(movies)
    serializer = AllMovieListSerializer(movies, many=True)
    for iidx in range(len(serializer.data)):
        genre_list, video_list = [], []
        for genre in dict(serializer.data[iidx])['genres']:
            genre_list.append(dict(genre)['genre_ids'])
        for idx, i in enumerate(genre_list):
            serializer.data[iidx]['genres'][idx] = i
            
        for video in dict(serializer.data[iidx])['videos']:
            video_list.append(dict(video))
        for v_idx, v in enumerate(video_list):
            serializer.data[iidx]['videos'][v_idx] = v['video']
    return Response(serializer.data)    

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie_detail = get_object_or_404(AllMovie, pk = movie_id)
    serializer = AllMovieListSerializer(movie_detail)
    return Response(serializer.data)
    
    
# @api_view(['GET'])
# def movie_detail(request, movie_id):
#     movie_detail = movie_detail_url(movie_id)
#     # print(movie_detail)
#     for md in movie_detail:
#         movies = MovieDetail()
#         movies.movie_id = md['movie_id']
#         movies.title = md['title']
#         movies.budget = md['budget']
#         movies.revenue = md['revenue']
#         movies.tagline = md['tagline']
#         movies.adult = md['adult']
#         movies.backdrop_path = md['backdrop_path']
#         movies.homepage = md['homepage']
#         movies.original_title =  md['original_title']
#         movies.overview = md['overview']
#         movies.popularity = md['popularity']
#         movies.poster_path = md['poster_path']
#         movies.release_date = md['release_date']
#         movies.runtime = md['runtime']
#         movies.vote_average = md['vote_average']
#         movies.video = md['videos']
#         movies.save()
#     # print('일단 movieset을 db에 저장함')
#     # print(movies)

#     serializer = MovieDetailSerializer(movies)
#     return Response(serializer.data)

@api_view(['GET'])
def today_movie_detail(request, movie_id):
    movie_detail = movie_detail_url(movie_id)
    for md in movie_detail:
        movies = MovieDetail()
        movies.movie_id = md['movie_id']
        movies.budget = md['budget']
        movies.revenue = md['revenue']
        movies.tagline = md['tagline']
        movies.adult = md['adult']
        movies.backdrop_path = md['backdrop_path']
        movies.homepage = md['homepage']
        movies.original_title =  md['original_title']
        movies.overview = md['overview']
        movies.popularity = md['popularity']
        movies.poster_path = md['poster_path']
        movies.release_date = md['release_date']
        movies.runtime = md['runtime']
        movies.vote_average = md['vote_average']
        movies.save()

    serializer = MovieDetailSerializer(movies)
    return Response(serializer.data)
    


@api_view(['GET'])
def comment_list(request, movie_id):
    if request.method == 'GET':
        movie = get_object_or_404(AllMovie, pk=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data['comment_set'])


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, movie_id, comments_pk):
    movie = get_object_or_404(AllMovie, pk = movie_id)
    comment = get_object_or_404(Comment, pk = comments_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        serializer = MovieSerializer(movie)
        return Response(serializer.data['comment_set'])

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, movie_pk):
    movie = get_object_or_404(AllMovie, pk=movie_pk)
    user = get_object_or_404(get_user_model(), pk = request.user.pk)
    serializer = CommentSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user = user, movie = movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def predict_movie(request):
    actors = request.data['actors']
    # actors = ['Victoria Garcia-Kelleher', 'Jordan Blair Mangold Brown']
    # print(actors)
    ymd = date.today()
    ymd = datetime.strftime(ymd, '%Y%m%d')
    today = ymd
    exchange_key = exchange_secret_key()
    exchange_rate_url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={}&searchdate={}&data=AP01'.format(exchange_key, today)
    exchange_res = requests.get(exchange_rate_url).text
    exchange_data = json.loads(exchange_res)
    exchange = "1,350"
    for find_data in exchange_data:
        if find_data['cur_unit'] == 'USD':
            exchange = find_data['kftc_bkpr']
    exchange = exchange.replace(',', '')
    check_all = []
    answer = 0
    answer_popular = 0
    for an in actors:
        actor1 = ActorList.objects.filter(actor_name=an)
        if not actor1:
            continue
        answer += int(actor1[0].actor_revenue) * int(actor1[0].actor_popularity)
        answer_popular += int(actor1[0].actor_popularity)
    if not answer:
        return Response(0)
    if answer_popular:
        answer = answer / answer_popular
    else:
        answer = answer / len(check_all)
    answer = answer * int(exchange)
    answer = format(int(answer), ',')
    return Response(answer)

@api_view(['GET', 'POST'])
def recommend_movie(request):
    movie = request.data['movie']
    recommend_list = []
    df = preprocess(movie)
    for idx in range(len(df)):
        movies = AllMovie.objects.filter(title=df[idx])
        recommend_list.append(movies[0])
    serializer = AllMovieListSerializer(recommend_list, many=True)
    for iidx in range(len(serializer.data)):
        genre_list, video_list = [], []
        for genre in dict(serializer.data[iidx])['genres']:
            genre_list.append(dict(genre)['genre_ids'])
        for idx, i in enumerate(genre_list):
            serializer.data[iidx]['genres'][idx] = i
            
        for video in dict(serializer.data[iidx])['videos']:
            video_list.append(dict(video))
        for v_idx, v in enumerate(video_list):
            serializer.data[iidx]['videos'][v_idx] = v['video']
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def profile_recommend_movie(request):
    movie = request.data['movie']
    recommend_list = []
    check = []
    for m in movie:
        check.append(m['title'])
    df = profileprocess(check)
    for idx in range(len(df)):
        movies = AllMovie.objects.filter(title=df[idx])
        recommend_list.append(movies[0])
    serializer = AllMovieListSerializer(recommend_list, many=True)
    for iidx in range(len(serializer.data)):
        genre_list, video_list = [], []
        for genre in dict(serializer.data[iidx])['genres']:
            genre_list.append(dict(genre)['genre_ids'])
        for idx, i in enumerate(genre_list):
            serializer.data[iidx]['genres'][idx] = i
            
        for video in dict(serializer.data[iidx])['videos']:
            video_list.append(dict(video))
        for v_idx, v in enumerate(video_list):
            serializer.data[iidx]['videos'][v_idx] = v['video']
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def movie_likes(request, movie_id):
    movie = AllMovie.objects.get(pk=movie_id)
    print(movie)
    user = get_object_or_404(get_user_model(), pk = request.user.pk)
    print(user)
    if movie.like_users.filter(pk = user.pk).exists():
        print('있으니 삭제')
        movie.like_users.remove(user)
    else:
        print('없으니 추가')
        movie.like_users.add(user)
    serializer = AllMovieListSerializer(movie)
    print(serializer.data)
    return Response(serializer.data)