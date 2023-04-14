import json



def max_revenue(movies):
    dic = {}
    for ids in movies:
        movie_id = ids['id']
        movie = json.load(open(f'data/movies/{movie_id}.json', encoding='utf-8'))
        movie_title = movie['title']
        movie_revenue = movie['revenue']
        dic[movie_title] = movie_revenue
    max_revenue = max(dic.values())
    for dic_max in dic:
        if dic[dic_max] == max_revenue:
            return dic_max

        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
