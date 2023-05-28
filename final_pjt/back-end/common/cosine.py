def preprocess(movie_name):
    import numpy as np
    from numpy import dot
    from numpy.linalg import norm
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import json
    from django.core.cache import cache

    # if cache.get(movie_name) or cache.get(movie_name) != None:
    #     return cache.get(movie_name)

    with open('./movies/fixtures/AllMovie.json', 'r', encoding='UTF-8') as f:
        today_movie_js = json.loads(f.read()) ## json 라이브러리 이용
    

    # DataFrame 생성
    df = pd.DataFrame(today_movie_js)

    # tfidf를 통하여 data 변환
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df['overview'])
    print(tfidf_matrix.shape)
    # cosine_similarity matrix 생성
    cosine_similar = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # title : index로 dictionary 생성
    cs_idx = dict(zip(df['title'], df.index))

    def get_recommendations(title, cosine_similar=cosine_similar):
        # 선택한 영화의 타이틀로부터 해당 영화의 인덱스를 받옴
        idx = cs_idx[title]

        # 해당 영화와 모든 영화와의 유사도를 가져옴
        sim_scores = list(enumerate(cosine_similar[idx]))

        # 유사도에 따라 영화들을 정렬
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # 가장 유사한 10개의 영화를 받아옴
        sim_scores = sim_scores[1:11]

        # 가장 유사한 10개의 영화의 인덱스를 얻음
        movie_indices = [idx[0] for idx in sim_scores]

        # 가장 유사한 10개의 영화의 제목을 리턴
        return df['title'].iloc[movie_indices]
    
    return_value = list(get_recommendations(movie_name))
    
    # for i in range(len(return_value)):
    #     cache.set(movie_name, return_value.iloc[i]['title'])
    #     print(cache)
    
    return return_value