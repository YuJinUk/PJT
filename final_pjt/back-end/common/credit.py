import json
import pandas as pd
import requests

def actor_list(movie_id, new_data={}):
    from detail import movie_detail_url
    import pandas as pd
    import json
    import requests
    
    my_api_key = "6a5ece7778e61cb35c55c953b8743b0d"
    
    url_credit = 'https://api.themoviedb.org/3/movie/'+ str(movie_id) +'/credits?api_key=' + my_api_key + '&language=en-US'
    res_credit = requests.get(url_credit).text
    data_credit = json.loads(res_credit) # 영화 참여자 목록
    #   "cast": [
    # {
    #   "adult": false,
    #   "gender": 2,
    #   "id": 13,
    #   "known_for_department": "Acting",
    #   "name": "Albert Brooks",
    #   "original_name": "Albert Brooks",
    #   "popularity": 8.633,
    #   "profile_path": "/8iDSGu5l93N7benjf6b3AysBore.jpg",
    #   "cast_id": 8,
    #   "character": "Marlin (voice)",
    #   "credit_id": "52fe420ec3a36847f8000679",
    #   "order": 0
    # },
    
    check_revenue = movie_detail_url(movie_id)
    movie_revenue = check_revenue[0]['revenue'] # 영화의 수익
    # print(movie_revenue)
    if not movie_revenue:
        return new_data
    
    for data in data_credit['cast']:
        if data['id'] not in new_data:
            new_data[data['id']] = {"name" : data['name'],
                                    "popularity" : data['popularity'],
                                    "movie_revenue" : [movie_revenue]}
        else:
            new_data[data['id']]['movie_revenue'].append(movie_revenue)
            
    # print(new_data)
    return new_data

with open('./movies/fixtures/all_movie.json', 'r', encoding='UTF-8') as f:
    all_movie_js = json.loads(f.read()) ## json 라이브러리 이용

new_data = {}
for movie in all_movie_js:
    new_data = actor_list(movie['fields']['movie_id'], new_data)
    # print(new_data)
    # break

final_data = []
for actor in new_data:
    val = new_data[actor]
    avg_revenue = sum(val['movie_revenue'])/len(val['movie_revenue'])
    val['movie_revenue'] = avg_revenue
    final_data.append(
        {
            "model": "movies.ActorList",
            "fields": {
                "actor_id": actor,
                "actor_name": val['name'],
                "actor_popularity": val['popularity'],
                "actor_revenue": avg_revenue,
            }
        }
    )
# print(final_data)

with open('./movies/fixtures/actor_list.json', 'w', encoding='UTF-8') as f:
    json.dump(final_data, f, ensure_ascii=False, indent=4)
