# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.best_movie_list), # 총점 상위 10개
    path('movies/page=<int:page_id>/', views.movie_page), # 모든 영화 page로 20개씩
    path('movies/today/', views.today_movie_list), # 오늘 상영하는 영화
    path('movies/<int:movie_id>/', views.movie_detail), # movies/detail
    path('movies/<int:movie_id>/likes/', views.movie_likes), # 영화 좋아요
    path('movies/today/<int:movie_id>/', views.today_movie_detail), # 오늘의 영화 detail
    path('movies/<int:movie_pk>/comments/', views.comment_create), # 영화에 댓글 추가
    path('movies/<int:movie_id>/allcomments/', views.comment_list), # 전체 댓글
    path('movies/<int:movie_id>/allcomments/<int:comments_pk>/', views.comment_detail), #댓삭
    path('movies/predicts/', views.predict_movie, name='predicts'), #영화 예측
    path('movies/recommends/', views.recommend_movie, name='recommend'), #영화 추천
    path('movies/recommends/profile/', views.profile_recommend_movie, name='profilerecommend'), #영화 추천
    # # 필수 작성
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]