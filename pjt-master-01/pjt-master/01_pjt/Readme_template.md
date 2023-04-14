>  PJT 작성 시 주의!
> 
> * 절대로 코드만 복붙하지 않는다.
> * 후기는 적어도 3줄은 씁시다!
> * 교수님이 안 볼 것 같지만 다 뜯어 봅니다.
> * 제출 당일 23:59분 내로 제출 합시다!
> * readme 없으면 일주일간 박제할 예정입니다. 
>   * 물론 readme 작성도 결국 해주셔야 합니다. 

# 

# PJT 01

### 이번 pjt 를 통해 배운 내용

* pjt 재미지구나

* ....

## A. 제공되는 영화 데이터의 주요내용 수집(problem_a)

* 요구 사항 : id,title,poster_path,vote_average,overview,genre_ids에 해당하는 value값 구하기



* 결과 : 
{'genre_ids': [18, 80],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
  
  * 문제 접근 방법 및 코드 설명
    * dictionary의 key : value에서 value를 호출하기 위해 key를 이용하고 result라는 새로운 dictionary에 key : value로 추가해주었습니다. 코드는 dictionary[key]를 통해 value를 호출했으며 result = { key : value(=dictionary[key])}를 통해 새로운 dictionary를 만들고 return했습니다.



```python
import json
from pprint import pprint

def movie_info(movie):
    result = {
        'id' : movie['id'],
        'title' : movie['title'],
        'poster_path' : movie.get('poster_path'), #해당 key가 있으면 해당 value를 반환, 없으면 None을 반환
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_ids' : movie.get('genre_ids')
    }
    return result


if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
```
  
  * 이 문제에서 어려웠던점
    * 교수님과 함께 진행했기 때문에 dictionary의 key : value구조와 호출원리를 다시 한 번 상기시킬 수 있었습니다.

  * 내가 생각하는 이 문제의 포인트
    * 앞서 말했듯이 dictionary의 구조와 원리입니다.


## B. 제공되는 영화 데이터의 주요 내용 수정(problem_b)

* 요구 사항 : A에서 구한 id,title,poster_path,vote_average,overview,genre_ids에서 genre_ids를 genre_names로 바꿔라

* 결과 : 
{'genre_names': ['Drama', 'Crime'],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
  
  * 문제 접근 방법 및 코드 설명
    * 공통점을 찾아 두 개의 문서에서 데이터를 비교 및 끌어오는 것입니다. 새로운 list인 name_list를 만들고 genres의 id가 movies의 genre_ids와 같으면 genres의 name을 호출하고 그 값을 result라는 dictionary에 추가해줍니다.


```python
import json
from pprint import pprint

# id,title,poster_path,vote_average,overview,genre_names

def movie_info(movie, genres):
    name_list = []
    for j in range(len(movie['genre_ids'])):
        for i in genres:
            if i['id'] == movie['genre_ids'][j]:
                name_list.append(i['name'])
    result = {
        'id' : movie['id'],
        'title' : movie['title'],
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_names' : name_list
    }
    return result

if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))  
```
  
  * 이 문제에서 어려웠던점
    * list와 dictionary의 호출 방법의 차이입니다. list의 경우 list[index]로 호출하고 dictionary의 경우 dictionary[key]로 호출합니다.

  * 내가 생각하는 이 문제의 포인트
    * list와 dictionary의 호출방법 및 for문과 if문의 활용입니다.


## C. 다중 데이터 분석 및 수정(problem_c)

* 요구 사항 : 평점이 높은 20개의 영화에 대하여 B의 작업을 실행시킵니다.

* 결과 : 
[{'genre_names': ['Drama', 'Crime'],
  'id': 278,
  'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
              '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
              '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
              '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
              '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
  'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
  'title': '쇼생크 탈출',
  'vote_average': 8.7},
 {'genre_names': ['Drama', 'Crime'],
  'id': 238,
  'overview': '시실리에서 이민온 뒤, 정치권까지 영향력을 미치는 거물로 자리잡은 돈 꼴레오네는 갖가지 고민을 호소하는 사람들의 '
              '문제를 해결해주며 대부라 불리운다. 한편 솔로소라는 인물은 꼴레오네가와 라이벌인 탓타리아 패밀리와 손잡고 새로운 '
              '마약 사업을 제안한다. 돈 꼴레오네가 마약 사업에 참여하지 않기로 하자, 돈 꼴레오네를 저격해 그는 중상을 입고 '
              '사경을 헤매게 된다. 그 뒤, 돈 꼴레오네의 아들 소니는 조직력을 총 동원해 다른 패밀리들과 피를 부르는 전쟁을 '
              '시작하는데... 가족의 사업과 상관없이 대학에 진학한 뒤 인텔리로 지내왔던 막내 아들 마이클은 아버지가 총격을 '
              '당한 뒤, 아버지를 구하기 위해 위험천만한 협상 자리에 나선다.',
  'poster_path': '/cOwVs8eYA4G9ZQs7hIRSoiZr46Q.jpg',
  'title': '대부',
  'vote_average': 8.7},
 {'genre_names': ['Drama', 'History', 'War'],
  'id': 424,
  'overview': '2차 세계대전 당시 독일군이 점령한 폴란드. 시류에 맞춰 자신의 성공을 추구하는 기회주의자 쉰들러는 유태인이 '
              '경영하는 그릇 공장을 인수한다. 그는 공장을 인수하기 위해 나찌 당원이 되고 독일군에게 뇌물을 바치는 등 갖은 '
...
              '되는데…',
  'poster_path': '/uw26mSTaA10hg2yuQfNaFLSeY3h.jpg',
  'title': '위대한 독재자',
  'vote_average': 8.4}]
  
  * 문제 접근 방법 및 코드 설명
    * B의 과정을 movies의 모든 dictionary에 적용시킨 후 리스트로 return합니다. 코드는 B를 for문에 추가하여 모든 영화에 적용시키는 내용입니다.
  
```python
import json
from pprint import pprint

# id,title,poster_path,vote_average,overview,genre_names

def movie_info(movies, genres):
    result_movies = []
    for movie in movies:
        name_list = []
        for j in range(len(movie['genre_ids'])):
            for i in genres:
                if i['id'] == movie['genre_ids'][j]:
                    name_list.append(i['name'])
                    
        result = {
            'id' : movie['id'],
            'title' : movie['title'],
            'poster_path' : movie.get('poster_path'),
            'vote_average' : movie.get('vote_average'),
            'overview' : movie.get('overview'),
            'genre_names' : name_list
        }
        result_movies.append(result)
    return result_movies    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```
  
  * 이 문제에서 어려웠던점
  
  * 내가 생각하는 이 문제의 포인트
    * 여러 dictionary가 하나의 list에 담겨 있을 때 하나씩 호출하여 적용시킨다.


## D. 알고리즘을 사용한 데이터 출력(problem_d)

* 요구 사항 : 수입이 가장 높은 movie를 return한다.

* 결과
  * 반지의 제왕: 왕의 귀환
  
  * 문제 접근 방법 및 코드 설명
    * 각 영화들의 id를 통해 세부정보를 불러온 후, title과 revenue를 호출하여 dictionary로 만듭니다. dictionary의 value 중 가장 큰 값을 찾아 key값을 return 시킵니다.
  
```python
import json

# 수입이 가장 높은 movie를 return한다.

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
```
  
  * 이 문제에서 어려웠던점
    * key : value로 작동하는 dictionary를 for문을 통해 value값을 통해 key값을 호출하는 것

  * 내가 생각하는 이 문제의 포인트
    * f-string과 dictionary를 for문을 통해 value값을 통해 key값을 호출하는 것


## E. 알고리즘을 사용한 데이터 출력(problem_e)

* 요구 사항 : 개봉 날짜 ; "release_date" 가 12월인 영화

* 결과
  * ['그린 마일', '인생은 아름다워', '반지의 제왕: 왕의 귀환', '스파이더맨: 뉴 유니버스']
  
  * 문제 접근 방법 및 코드 설명
    * 영화의 release_date의 문자열 중 index가 5,6이 월을 나타낸다는 점을 기반으로 if문을 통해 12월이면 호출하여 movie_list에 추가한다. 
  
```python
import json

# 개봉 날짜 ; "release_date" 가 12월인 영화

def dec_movies(movies):
    movie_list = []
    for ids in movies:
        movie_id = ids['id']
        movie = json.load(open(f'data/movies/{movie_id}.json', encoding='utf-8'))
        movie_title = movie['title']
        movie_date = movie['release_date']
        if movie_date[5:7] == '12':
            movie_list.append(movie_title)
    return movie_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))   
```
  
  * 이 문제에서 어려웠던점
    * index를 통하여 문자열을 호출
  * 내가 생각하는 이 문제의 포인트
    * 문자열 또한 index로 부분만 호출할 수 있음.



....

문제 푼 내용을 기반으로 적어주세요.

# 후기

* json의 데이터를 통해 여러 데이터를 통합하거나 연결하여 원하는 결과값을 찾아가는 과정이 흥미로웠습니다.