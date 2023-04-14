#F 2
import json
# 90년대 개봉작 중 많은 수입을 올린 영화 순위
 
def movie_90(movies):

    dic = {}
    return_list = []

    for ids in movies:
        movie_id = ids['id']
        movie = json.load(open(f'data/movies/{movie_id}.json', encoding='utf-8'))
        movie_title = movie['title']
        movie_revenue = movie['revenue']
        movie_date = movie['release_date']
        if movie_date[:3] in str(range(1990,2000)):
            dic[movie_title] = movie_revenue

    revenue_order = sorted(dic.values())
    n = len(revenue_order)
    award = {}

    for dic_key in dic:
        for i in range(n):
            if dic[dic_key] == revenue_order[i]:
                award[f'{n-i}위'] = dic_key
    
    return award

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(movie_90(movies_list))