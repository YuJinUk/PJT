def profileprocess(movie_list):
    import numpy as np
    from numpy import dot
    from numpy.linalg import norm
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import json
    # from django.core.cache import cache

    # if cache.get(movie_name) or cache.get(movie_name) != None:
    #     return cache.get(movie_name)

    
    with open('./movies/fixtures/AllMovie.json', 'r', encoding='UTF-8') as f:
        today_movie_js = json.loads(f.read()) ## json 라이브러리 이용
    
    print('profileporcess에 들어옴')
    print(movie_list)
    # DataFrame 생성
    df = pd.DataFrame(today_movie_js)
    
    new_movie_name = ''
    new_df = df['overview']
    new_overview = []
    
    for movie in movie_list:
        new_overview += list(df[df['title'] == movie]['overview'])
        new_movie_name += movie
    
    new_df.loc[len(new_df)+1] = str(new_overview)
    
    
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(new_df)
    

    # cosine_similarity matrix 생성
    cosine_similar = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # title : index로 dictionary 생성
    cs_idx = dict(zip(df['title'], df.index))
    cs_idx[new_movie_name] = len(cs_idx)
    
    def get_recommendations(title, cosine_similar=cosine_similar):
        # 선택한 영화의 타이틀로부터 해당 영화의 인덱스를 받옴
        idx = cs_idx[title]

        # 해당 영화와 모든 영화와의 유사도를 가져옴
        sim_scores = list(enumerate(cosine_similar[idx]))
        # print(sim_scores)

        # 유사도에 따라 영화들을 정렬
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        # 가장 유사한 10개의 영화를 받아옴
        random_num = np.random.randint(1, 500, size=10)
        print(random_num)
        check = []
        for num in random_num:
            check.append(sim_scores[num])
        sim_scores = check

        # 가장 유사한 10개의 영화의 인덱스를 얻음
        movie_indices = [idx[0] for idx in sim_scores]

        # 가장 유사한 10개의 영화의 제목을 리턴
        return df['title'].iloc[movie_indices]
    
    return_value = list(get_recommendations(new_movie_name))
    
    return return_value