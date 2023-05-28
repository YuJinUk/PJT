def movie_detail_url(movie_id):
    import pandas as pd
    import json
    import requests
    
    my_api_key = "6a5ece7778e61cb35c55c953b8743b0d"
    url = 'https://api.themoviedb.org/3/movie/'+ str(movie_id) +'?api_key=' + my_api_key + '&language=ko-KR'
    res = requests.get(url).text
    data = json.loads(res)
    # print(data)
    
    video_url = 'https://api.themoviedb.org/3/movie/' + str(movie_id) + '/videos?api_key=' + my_api_key +'&language=en-US'
    video_res = requests.get(video_url).text
    video_data = json.loads(video_res)
    video_data = video_data['results'][:5]
    
    yt_url_list = []

    for video_key in video_data:
        video_key = video_key['key']
        yt_url = 'https://www.youtube.com/watch?v=' + video_key
        yt_url_list.append(yt_url)
    
    if data['backdrop_path']:
        data['backdrop_path'] = 'https://image.tmdb.org/t/p/original' + data['backdrop_path']
    if data['poster_path']:
        data['poster_path'] = 'https://image.tmdb.org/t/p/original' + data['poster_path']
    for idx, genre in enumerate(data['genres']):
        data['genres'][idx] = genre['name']
        
    
    new_data = [
        {
            'movie_id': data['id'],
            'budget': data['budget'],
            'revenue': data['revenue'],
            'tagline': data['tagline'],
            'adult': data['adult'],
            'backdrop_path': data['backdrop_path'],
            'homepage': data['homepage'],
            'original_title': data['original_title'],
            'overview': data['overview'],
            'popularity': data['popularity'],
            'poster_path': data['poster_path'],
            'release_date': data['release_date'],
            'runtime': data['runtime'],
            'vote_average': data['vote_average'],
            'title': data['title'],
            'videos': yt_url_list,
        }
    ]
    return new_data