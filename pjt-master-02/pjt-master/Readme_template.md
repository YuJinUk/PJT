>  PJT 작성 시 주의!
> 
> * 절대로 코드만 복붙하지 않는다.
> * 후기는 적어도 3줄은 씁시다!
> * 교수님이 안 볼 것 같지만 다 뜯어 봅니다.
> * 제출 당일 23:59분 내로 제출 합시다!
> * readme 없으면 일주일간 박제할 예정입니다. 
>   * 물론 readme 작성도 결국 해주셔야 합니다. 

# 

# PJT 02

### 이번 pjt 를 통해 배운 내용

* api 이용방법


## A. 인기 영화 조회

* 요구 사항 : 인기 영화 목록을 응답 받아 개수를 출력합니다.

* 결과 : 20
  
  * 문제 접근 방법 및 코드 설명
    * url과 parameter을 이용하여 불러오고 결과값의 길이를 return
  
```python
def popular_count():
    movie_code = 'popular'

    URL = f'https://api.themoviedb.org/3/movie/{movie_code}'

    param= {
    'api_key' : '6a5ece7778e61cb35c55c953b8743b0d',
    'language' : 'ko-KR',
    'region' : 'KR'
    }

    r = requests.get(URL, params = param).json()

    return len(r['results'])

```
  
  * 이 문제에서 어려웠던점
    * requests의 사용
  * 내가 생각하는 이 문제의 포인트
    * requests 사용법

## B. 특정 조건에 맞는 인기 영화 조회 1

* 요구 사항 : 인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력합니다.

* 결과 : 
  [{'adult': False,
    'backdrop_path': '/faXT8V80JRhnArTAeYXz0Eutpv9.jpg',
    'genre_ids': [16, 28, 12, 35, 10751, 14],
    'id': 315162,
    'original_language': 'en',
    'original_title': 'Puss in Boots: The Last Wish',
    'overview': '아홉 개의 목숨 중 단 하나의 목숨만 남은 장화신은 고양이
  .  마지막 남은 목숨을 지키기 위해 히어로의 삶 대신 '
                '반려묘의 삶을 선택한 그에게 찾아온 마지막 기회, 바로 소
  원을 들어주는 소원별이 있는 곳을 알려주는 지도!  '
                "잃어버린 목숨을 되찾고 다시 히어로가 되기를 꿈꾸는 장화
  신은 고양이는 뜻밖에 동료가 된 앙숙 파트너 '키티 "
                "말랑손', 그저 친구들과 함께라면 모든 게 행복한 강아지 '페로'와 함께 소원별을 찾기 위해 길을 떠난다.  "
                '그리고 소원별을 노리는 또 다른 빌런들과 마주치게 되는데
  …',
    'popularity': 5946.788,
    'poster_path': '/rKgvctIuPXyuqOzCQ16VGdnHxKx.jpg',
    'release_date': '2023-01-04',
    'title': '장화신은 고양이: 끝내주는 모험',
    'video': False,
    'vote_average': 8.6,
    'vote_count': 2658},
  {'adult': False,
    'backdrop_path': '/e782pDRAlu4BG0ahd777n8zfPzZ.jpg',
    'genre_ids': [16, 14, 18],
    'id': 555604,
    'original_language': 'en',
    'original_title': "Guillermo del Toro's Pinocchio",
    'overview': '많은 이들의 사랑을 받은 목각 인형 피노키오의 마법 같은 
  모험. 현실의 한계를 뛰어넘어, 새 생명을 불어넣는 '
                '강력한 사랑의 힘이 펼쳐진다. 이탈리아 고전 동화 "피노키
  오"가 스톱모션 뮤지컬로 재탄생한다. 말썽꾸러기 '
                '피노키오는 과연 인간 소년이 될 수 있을까? 그 여정을 따 
  라가 보자.',
    'popularity': 713.806,
    'poster_path': '/6bdUtxydFXLtgcxHMMvlkNnRZWg.jpg',
    'release_date': '2022-11-23',
    'title': '기예르모 델토로의 피노키오',
    'video': False,
    'vote_average': 8.4,
    'vote_count': 1675}]
  
  * 문제 접근 방법 및 코드 설명
    * url과 parameter을 이용하여 불러오고 list 및 dictionary의 호출을 이용하여 return
  
```python
def vote_average_movies():
  movie_code = 'popular'

  URL = f'https://api.themoviedb.org/3/movie/{movie_code}'

  param= {
    'api_key' : '6a5ece7778e61cb35c55c953b8743b0d',
    'language' : 'ko-KR',
    'region' : 'KR'
  }

  r = requests.get(URL, params = param).json()['results']

  result = []
  for movie in r:
    if movie['vote_average'] >= 8:
      result.append(movie)
  
  return result
```
  
  * 이 문제에서 어려웠던점
    * requests의 사용
  * 내가 생각하는 이 문제의 포인트
    * requests 사용법


## C. 특정 조건에 맞는 인기 영화 조회 2

* 요구 사항 : 인기 영화 목록을 평점이 높은 순으로 5개의 영화 데이터 목록을 출력합니다.

* 결과 :
  [{'adult': False,
    'backdrop_path': '/faXT8V80JRhnArTAeYXz0Eutpv9.jpg',
    'genre_ids': [16, 28, 12, 35, 10751, 14],
    'id': 315162,
    'original_language': 'en',
    'original_title': 'Puss in Boots: The Last Wish',
    'overview': '아홉 개의 목숨 중 단 하나의 목숨만 남은 장화신은 고양이
  .  마지막 남은 목숨을 지키기 위해 히어로의 삶 대신 '
                '반려묘의 삶을 선택한 그에게 찾아온 마지막 기회, 바로 소
  원을 들어주는 소원별이 있는 곳을 알려주는 지도!  '
                "잃어버린 목숨을 되찾고 다시 히어로가 되기를 꿈꾸는 장화
  신은 고양이는 뜻밖에 동료가 된 앙숙 파트너 '키티 "
                "말랑손', 그저 친구들과 함께라면 모든 게 행복한 강아지 '페로'와 함께 소원별을 찾기 위해 길을 떠난다.  "
                '그리고 소원별을 노리는 또 다른 빌런들과 마주치게 되는데
  …',
    'popularity': 5946.788,
    'poster_path': '/rKgvctIuPXyuqOzCQ16VGdnHxKx.jpg',
    'release_date': '2023-01-04',
    'title': '장화신은 고양이: 끝내주는 모험',
    'video': False,
    'vote_average': 8.6,
    'vote_count': 2658},
  {'adult': False,
    'backdrop_path': '/e782pDRAlu4BG0ahd777n8zfPzZ.jpg',
    'genre_ids': [16, 14, 18],
    'id': 555604,
    'original_language': 'en',
    'original_title': "Guillermo del Toro's Pinocchio",
    'overview': '많은 이들의 사랑을 받은 목각 인형 피노키오의 마법 같은 
  모험. 현실의 한계를 뛰어넘어, 새 생명을 불어넣는 '
                '강력한 사랑의 힘이 펼쳐진다. 이탈리아 고전 동화 "피노키
  오"가 스톱모션 뮤지컬로 재탄생한다. 말썽꾸러기 '
                '피노키오는 과연 인간 소년이 될 수 있을까? 그 여정을 따 
  라가 보자.',
    'popularity': 713.806,
    'poster_path': '/6bdUtxydFXLtgcxHMMvlkNnRZWg.jpg',
    'release_date': '2022-11-23',
    'title': '기예르모 델토로의 피노키오',
    'video': False,
    'vote_average': 8.4,
    'vote_count': 1675},
  {'adult': False,
    'backdrop_path': '/s16H6tpK2utvwDtzZ8Qy4qm5Emw.jpg',
    'genre_ids': [878, 12, 28],
    'id': 76600,
    'original_language': 'en',
    'original_title': 'Avatar: The Way of Water',
    'overview': '판도라 행성에서 제이크 설리와 네이티리가 이룬 가족이 겪
  게 되는 무자비한 위협과 살아남기 위해 떠나야 하는 긴 '
                '여정과 전투, 그리고 견뎌내야 할 상처에 대한 이야기를 그
  렸다. 살아남기 위해 설리 가족이 숲에서 바다로 터전을 '
                '옮기면서 겪게 되는 화합의 과정, 그리고 곳곳에서 도사리 
  는 새로운 위협까지 역경 속에서 더 아름답게 펼쳐진다.',
    'popularity': 2391.76,
    'poster_path': '/z56bVX93oRG6uDeMACR7cXCnAbh.jpg',
    'release_date': '2022-12-14',
    'title': '아바타: 물의 길',
    'video': False,
    'vote_average': 7.7,
    'vote_count': 4671},
  {'adult': False,
    'backdrop_path': '/8I37NtDffNV7AZlDa7uDvvqhovU.jpg',
    'genre_ids': [28, 12, 14, 878],
    'id': 19995,
    'original_language': 'en',
    'original_title': 'Avatar',
    'overview': '가까운 미래, 지구는 에너지 고갈 문제를 해결하기 위해 머
  나먼 행성 판도라에서 대체 자원을 채굴하기 시작한다. '
                '하지만 판도라의 독성을 지닌 대기로 인해 자원 획득에 어 
  려움을 겪게 된 인류는 판도라의 토착민 나비의 외형에 '
                '인간의 의식을 주입, 원격 조종이 가능한 새로운 생명체를 
  탄생시키는 프로그램을 개발한다. 한편 하반신이 마비된 '
                '전직 해병대원 제이크 설리는 아바타 프로그램에 참가할 것
  을 제안받는다. 그 곳에서 자신의 아바타를 통해 자유롭게 '
                '걸을 수 있게 된 제이크는 자원 채굴을 막으려는 나비의 무
  리에 침투하라는 임무를 부여받는데...',
    'popularity': 1145.042,
    'poster_path': '/zygmx5abXeDpr3fWYX4jlXFZ1wh.jpg',
    'release_date': '2009-12-17',
    'title': '아바타',
    'video': False,
    'vote_average': 7.6,
    'vote_count': 28031},
  {'adult': False,
    'backdrop_path': '/yYrvN5WFeGYjJnRzhY0QXuo4Isw.jpg',
    'genre_ids': [28, 12, 878],
    'id': 505642,
    'original_language': 'en',
    'original_title': 'Black Panther: Wakanda Forever',
    'overview': '국왕이자 블랙 팬서인 티찰라의 죽음 이후 수많은 강대국으
  로부터 위협을 받게 된 와칸다. 라몬다, 슈리 그리고 '
                '나키아, 오코예, 음바쿠는 각자 사명감을 갖고 와칸다를 지
  키기 위해 외로운 싸움을 이어간다. 한편, 비브라늄의 '
                '패권을 둘러싼 미스터리한 음모와 함께 깊은 해저에서 모습
  을 드러낸 최강의 적 네이머와 탈로칸의 전사들은 와칸다를 '
                '향해 무차별 공격을 퍼붓기 시작하는데…',
    'popularity': 1160.142,
    'poster_path': '/3PCRWLeqp5y20k6XVzcamZR3BWF.jpg',
    'release_date': '2022-11-09',
    'title': '블랙 팬서: 와칸다 포에버',
    'video': False,
    'vote_average': 7.5,
    'vote_count': 1708}]
  
  * 문제 접근 방법 및 코드 설명
    * url과 parameter을 이용하여 불러오고 결과값의 길이를 return
  
```python
def ranking():
  movie_code = 'popular'

  URL = f'https://api.themoviedb.org/3/movie/{movie_code}'
  
  param= {
    'api_key' : '6a5ece7778e61cb35c55c953b8743b0d',
    'language' : 'ko-KR',
    'region' : 'KR'
  }
  
  r = requests.get(URL, params = param).json()['results']

  return sorted(r, key = lambda x : x['vote_average'], reverse = True)[:5]


```
  
  * 이 문제에서 어려웠던점
    * requests의 사용
  * 내가 생각하는 이 문제의 포인트
    * requests 사용 및 sorted에서의 lambda사용법

## D. 특정 추천 영화 조회

* 요구 사항 : 제공된 영화 제목을 검색하여 추천 영화 목록을 출력합니다.

* 결과
  [{'adult': False,
    'backdrop_path': '/2Xe9lISpwXKhvKiHttbFfVRERQX.jpg',
    'genre_ids': [18, 35],
    'id': 490132,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': 'Green Book',
    'overview': '1962년 미국, 입담과 주먹만 믿고 살아가던 토니 발레롱가 
  는 교양과 우아함 그 자체인 천재 피아니스트 돈 셜리의 '
                '운전기사 면접을 보게 된다. 백악관에도 초청되는 등 미국 
  전역에서 콘서트 요청을 받으며 명성을 떨치고 있는 돈 '
                '셜리는 위험하기로 소문난 미국 남부 투어 공연을 떠나기로
  결심하고, 투어 기간 동안 자신의 보디가드 겸 운전기사로 '
                '토니를 고용한다. 거친 인생을 살아온 토니와 교양과 기품 
  을 지키며 살아온 돈. 생각, 행동, 말투, 취향까지 '
                '달라도 너무 다른 두 사람은 그들을 위한 여행안내서 그린 
  북에 의존해 특별한 남부 투어를 시작하는데...',
    'popularity': 40.32,
    'poster_path': '/dyqQ12gZGwl5Y0R9UsLBDkZWOUA.jpg',
    'release_date': '2018-11-16',
    'title': '그린 북',
    'video': False,
    'vote_average': 8.237,
    'vote_count': 9763},
  {'adult': False,
    'backdrop_path': None,
    'genre_ids': [],
    'id': 642721,
    'media_type': 'movie',
    'original_language': 'ar',
    'original_title': 'Awdat Al-Rouh',
    'overview': '',
    'popularity': 0.6,
    'poster_path': '/mOpHGETnYr1OgQifBb7xk59N5Il.jpg',
    'release_date': '',
    'title': 'Awdat Al-Rouh',
    'video': False,
    'vote_average': 0.0,
    'vote_count': 0},
  {'adult': False,
    'backdrop_path': '/hO7KbdvGOtDdeg0W4Y5nKEHeDDh.jpg',
    'genre_ids': [80, 53, 18],
    'id': 475557,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': 'Joker',
    'overview': '홀어머니와 사는 아서 플렉은 코미디언을 꿈꾸지만 그의 삶
  은 좌절과 절망으로 가득 차 있다. 광대 아르바이트는 '
                '그에게 모욕을 가져다주기 일쑤고, 긴장하면 웃음을 통제할
  수 없는 신경병 증세는 그를 더욱 고립시킨다. 정부 예산 '
                '긴축으로 인해 정신과 약물을 지원하던 공공의료 서비스마 
  저 없어져 버린 어느 날, 아서는 지하철에서 시비를 걸어온 '
                '증권사 직원들에게 얻어맞던 와중에 동료가 건네준 권총으 
  로 그들을 쏴 버리고 만다. 군중들은 지배계급에 대한 저항의 '
                '아이콘이 된 그를 추종하기 시작하며 광대 마스크로 얼굴을
  가리고 거리로 쏟아져 나오기 시작하는데...',
    'popularity': 74.743,
    'poster_path': '/wrCwH6WOvXQvVuqcKNUrLDCDxdw.jpg',
    'release_date': '2019-10-01',
    'title': '조커',
    'video': False,
    'vote_average': 8.171,
    'vote_count': 22056},
  {'adult': False,
    'backdrop_path': '/oRiUKwDpcqDdoLwPoA4FIRh3hqY.jpg',
    'genre_ids': [35, 18, 53],
    'id': 466272,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': 'Once Upon a Time… in Hollywood',
    'overview': '자유의 바람이 불던 1969년 할리우드, 잊혀져 가는 액션스 
  타 릭 달튼과 그의 스턴트 배우 겸 매니저인 클리프 '
                '부스는 과거의 영광을 되찾기 위해 고군분투하지만 새로운 
  스타들에 밀려 큰 성과를 거두진 못한다. 어느 날 릭의 '
                '옆집에 할리우드에서 가장 핫한 로만 폴란스키 감독과 배우
  샤론 테이트 부부가 이사 오자 릭은 새로운 기회가 생길 '
                '수도 있다고 기뻐하지만 인사조차 나누지 못한다. 형편상  
  더 이상 함께 일할 수 없게 된 릭과 클리프는 각자의 길을 '
                '가기로 하고 릭의 집에서 술을 거나하게 마시던 중 뜻하지 
  않은 낯선 방문객을 맞이하게 되는데…',
    'popularity': 35.39,
    'poster_path': '/1F2rDT1oNdvMyXF7gxbGxaXCzrz.jpg',
    'release_date': '2019-07-24',
    'title': '원스 어폰 어 타임 인… 할리우드',
    'video': False,
    'vote_average': 7.435,
    'vote_count': 11391},
  {'adult': False,
    'backdrop_path': '/2lBOQK06tltt8SQaswgb8d657Mv.jpg',
    'genre_ids': [10752, 18, 36],
    'id': 530915,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': '1917',
    'overview': '제1차 세계대전이 한창인 1917년 4월 6일. 독일군에 의해  
  모든 통신망이 파괴된 상황 속에서 서부전선의 영국군 '
                '병사 스코필드와 블레이크에게 하나의 미션이 주어졌다. 독
  일군의 함정에 빠진 영국군 부대의 수장 매켄지 중령에게 '
                '에린무어 장군의 공격 중지 명령을 전달하라는 것. 블레이 
  크는 데본셔 연대에 있는 형을 구하기 위해 기꺼이 임무를 '
                '수행한다. 동료인 스코필드는 처음엔 당황스러워하지만 이 
  내 1600명의 동료들을 구하기 위해 전쟁터 한가운데를 '
                '가로지르는 여정에 동참한다.',
    'popularity': 51.278,
    'poster_path': '/u2oRQqUashBBIj5UNeOd5TN0bmB.jpg',
    'release_date': '2019-12-25',
    'title': '1917',
    'video': False,
    'vote_average': 7.983,
    'vote_count': 10640},
  {'adult': False,
    'backdrop_path': '/agoBZfL1q5G79SD0npArSlJn8BH.jpg',
    'genre_ids': [35, 10752, 18],
    'id': 515001,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': 'Jojo Rabbit',
    'overview': '전쟁이 막바지에 접어든 1940년대 독일, 엄마 로지와 단둘 
  이 살고 있는 10살 소년 조조는 독일 소년단에 '
                '입단한다. 상상 속 친구 히틀러의 응원에 힘입어 소년단 생
  활을 시작한 조조는 나약한 모습으로 단원 사이에서 '
                '놀림거리가 되고 만다. 설상가상으로 조조는 수류탄 사고까
  지 일으키며 얼굴과 다리에 부상을 입는다. 그렇게 히틀러의 '
                '멋진 경호원이 되겠다는 부푼 꿈이 물거품으로 돌아갈 때쯤
  , 조조는 자신의 집 벽장 안에 숨어 지내던 유대인 소녀 '
                '엘사와 마주치게 되는데...',
    'popularity': 36.555,
    'poster_path': '/vUDIREXlBiGT1WoKNVaV47gdtkA.jpg',
    'release_date': '2019-10-18',
    'title': '조조 래빗',
    'video': False,
    'vote_average': 8.061,
    'vote_count': 8110},
  {'adult': False,
    'backdrop_path': None,
    'genre_ids': [10402],
    'id': 365297,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': 'My Chemical Romance: AOL Sessions',
    'overview': 'AOL Sessions is a video release of the live Sessions@AOL '
                'performances by American rock band My Chemical Romance. The '
                'album features six videos, all of which are songs from 
  the '
                "band's third studio album, The Black Parade.",
    'popularity': 0.902,
    'poster_path': '/iqoNZKyfqUMRKKo0VZOaGyMrF9g.jpg',
    'release_date': '2007-12-18',
    'title': 'My Chemical Romance: AOL Sessions',
    'video': True,
    'vote_average': 10.0,
    'vote_count': 2},
  {'adult': False,
    'backdrop_path': None,
    'genre_ids': [99],
    'id': 887731,
    'media_type': 'movie',
    'original_language': 'ar',
    'original_title': 'Al Awda',
    'overview': 'Due to the impact of the global Coronavirus pandemic, the '
                'author of the film comes back to her birthplace after having '
                'spent the last 10 years abroad. She goes about her daily '
                'routine under lockdown along with her parents: her father '
                'teeming with good humour who takes government restrictions with '
                'reservations, and her mother who voluntarily locks herself in '
                'her room because of fears she could infect other flatmates with '
                'the virus she may not even have. Sara Shazli observes city '
                'bustle outside the windows and domestic life through the camera '
                'lens in her own perspective, treating familiar situations with '
                'both tragic and comic distance. Being locked down with 
  her '
                'parents helps her in rediscovering family ties and her 
  '
                'relationship to home.',
    'popularity': 1.38,
    'poster_path': None,
    'release_date': '2021-10-21',
    'title': 'Back Home',
    'video': False,
    'vote_average': 0.0,
    'vote_count': 0},
  {'adult': False,
    'backdrop_path': '/4PCO7tewIGnE6ySjVf2DbJ3pjqq.jpg',
    'genre_ids': [18],
    'id': 492188,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': 'Marriage Story',
    'overview': '한때 스타였지만 지금은 남편에게 가려진 연극배우 니콜과 
  브로드웨이에서 잘나가는 연출가 찰리는 9년 여에 걸친 결혼 '
                '생활을 정리하고 이혼을 준비 중이다. 서로에 대한 존중으
  로 원만한 이혼을 계획하지만 합의 과정이 쉽지만은 않다. '
                '니콜은 드라마 촬영을 이유로 뉴욕을 떠나 고향 LA로 이주 
  하고, 그곳에서 찰리에게 이혼 소송을 제기한다. 찰리는 '
                '아들의 양육권을 얻기 위해 LA와 뉴욕을 오가며 소송에 임 
  한다. 파경을 맞았지만 관계를 유지해야 하는 한 가족을 '
                '예리하고도 따뜻한 시선으로 바라본다.',
    'popularity': 22.17,
    'poster_path': '/solGqhXDHo4tS6edTf5IkTblbc1.jpg',
    'release_date': '2019-09-28',
    'title': '결혼 이야기',
    'video': False,
    'vote_average': 7.755,
    'vote_count': 6129},
  {'adult': False,
    'backdrop_path': '/4HWAQu28e2yaWrtupFPGFkdNU7V.jpg',
    'genre_ids': [35, 80, 9648],
    'id': 546554,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': 'Knives Out',
    'overview': '미스터리 소설의 대가인 작가 할란이 자신의 85살 생일에  
  자신의 방에서 날카로운 단검으로 목이 그인 채 발견된다. '
                '외딴 저택에 모인 할란의 간병인과 자식 내외, 그리고 3세 
  들은 유산 상속을 놓고 대거 혼란에 빠진다. 파견된 '
                '형사들은 가족과의 면담을 할 수록 자살로 의견이 모이지만
  , 면담 중 멀찍이 떨어져 상황을 전망하는 푸른 눈의 '
                '사내는 형사들마저 압도하며 심문을 주도해나간다. 남자의 
  이름은 바로 브누아 블랑. 챔피언 사건을 해결해서 이름이 '
                '높아진 유명한 사립탐정이다.',
    'popularity': 75.8,
    'poster_path': '/7brBiaaH1sToGV1YBi5EIUnyjo0.jpg',
    'release_date': '2019-11-27',
    'title': '나이브스 아웃',
    'video': False,
    'vote_average': 7.855,
    'vote_count': 10213},
  {'adult': False,
    'backdrop_path': '/tmU7GeKVybMWFButWEGl2M4GeiP.jpg',
    'genre_ids': [18, 80],
    'id': 238,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': 'The Godfather',
    'overview': '시실리에서 이민온 뒤, 정치권까지 영향력을 미치는 거물로
  자리잡은 돈 꼴레오네는 갖가지 고민을 호소하는 사람들의 '
                '문제를 해결해주며 대부라 불리운다. 한편 솔로소라는 인물
  은 꼴레오네가와 라이벌인 탓타리아 패밀리와 손잡고 새로운 '
                '마약 사업을 제안한다. 돈 꼴레오네가 마약 사업에 참여하 
  지 않기로 하자, 돈 꼴레오네를 저격해 그는 중상을 입고 '
                '사경을 헤매게 된다. 그 뒤, 돈 꼴레오네의 아들 소니는 조
  직력을 총 동원해 다른 패밀리들과 피를 부르는 전쟁을 '
                '시작하는데... 가족의 사업과 상관없이 대학에 진학한 뒤  
  인텔리로 지내왔던 막내 아들 마이클은 아버지가 총격을 '
                '당한 뒤, 아버지를 구하기 위해 위험천만한 협상 자리에 나
  선다.',
    'popularity': 96.894,
    'poster_path': '/cOwVs8eYA4G9ZQs7hIRSoiZr46Q.jpg',
    'release_date': '1972-03-14',
    'title': '대부',
    'video': False,
    'vote_average': 8.714,
    'vote_count': 17364},
  {'adult': False,
    'backdrop_path': '/8qbpFixlUbsyZjQhQbsFrnLmJSw.jpg',
    'genre_ids': [80, 18, 36],
    'id': 398978,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': 'The Irishman',
    'overview': '2000년, 양로원에서 쓸쓸하게 늙어가는 프랭크 시런은 1975년 빌 버팔리노의 딸 결혼식 참석을 위해 길을 '
                '떠났던 날을 회상한다. 영화는 제2차 세계대전에 참전했던 
  노동자 출신의 프랭크가 어떻게 청부살인업자로 활약하게 '
                '됐는지 따라가며 주변 인물과 관계를 조명한다. 지미 호파 
  는 전미운수노조의 수장으로서 막강한 권력을 누리고, 프랭크 '
                '시런을 범죄로 끌어들인 러셀 버팔리노는 살해 건수를 배당
  하는 설계자다. 법무장관으로 지명된 로버트 케네디의 견제, '
                '그로 인한 지미의 감옥행은 나비효과처럼 예기치 못한 결과
  로 이어지는데...',
    'popularity': 29.247,
    'poster_path': '/Ch4DTlESeylOs7VaTI5YWI2XN9.jpg',
    'release_date': '2019-11-01',
    'title': '아이리시맨',
    'video': False,
    'vote_average': 7.627,
    'vote_count': 5825},
  {'adult': False,
    'backdrop_path': '/Ab8mkHmkYADjU7wQiOkia9BzGvS.jpg',
    'genre_ids': [16, 10751, 14],
    'id': 129,
    'media_type': 'movie',
    'original_language': 'ja',
    'original_title': '千と千尋の神隠し',
    'overview': '평범한 열 살 짜리 소녀 치히로 식구는 이사 가던 중 길을 
  잘못 들어 낡은 터널을 지나가게 된다. 터널 저편엔 '
                '폐허가 된 놀이공원이 있었고 그곳엔 이상한 기운이 흘렀다
  . 인기척 하나 없는 이 마을의 낯선 분위기에 불길한 '
                '기운을 느낀 치히로는 부모님에게 돌아가자고 조르지만 부 
  모님은 호기심에 들떠 마을 곳곳을 돌아다니기 시작한다. 어느 '
                '음식점에 도착한 치히로의 부모님은 그 곳에 차려진 음식들
  을 보고 즐거워하며 허겁지겁 먹어대다가 돼지로 변해버린다. '
                '겁에 질려 당황하는 치히로에게 낯선 소년 하쿠가 나타나  
  빨리 이곳을 나가라고 소리치는데...',
    'popularity': 71.212,
    'poster_path': '/u1L4qxIu5sC2P082uMHYt7Ifvnj.jpg',
    'release_date': '2002-09-20',
    'title': '센과 치히로의 행방불명',
    'video': False,
    'vote_average': 8.539,
    'vote_count': 13856},
  {'adult': False,
    'backdrop_path': '/20GagiVvyqvWYxIGEFFVDa934n.jpg',
    'genre_ids': [28],
    'id': 138037,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': 'The Wrestling Classic',
    'overview': 'The Wrestling Classic was a World Wrestling Federation 
  '
                'pay-per-view event that took place on November 7, 1985 
  from the '
                'Rosemont Horizon in Rosemont, Illinois. The main event 
  was the '
                'finals of a 16-man tournament where Junkyard Dog defeated Randy '
                'Savage. The undercard featured a 16-man single-elimination '
                'tournament, Hulk Hogan versus Roddy Piper for the WWF '              'Championship and a contest where Michael Hamley won a Rolls '
                'Royce.',
    'popularity': 1.691,
    'poster_path': '/65leMru9sbN9Es33VtCAchEf66s.jpg',
    'release_date': '1985-11-07',
    'title': 'The Wrestling Classic',
    'video': True,
    'vote_average': 6.1,
    'vote_count': 8},
  {'adult': False,
    'backdrop_path': '/qvaOdpQqygDFi0KZnWdcjO3mk3C.jpg',
    'genre_ids': [],
    'id': 170787,
    'media_type': 'movie',
    'original_language': 'zh',
    'original_title': '股瘋',
    'overview': 'Pan Hung is Lily, a humble bus conductor hired by Hong 
  Kong '
                'commodities trader Sean Lau to be his connection to the '
                'Shanghai stock market. Lily finds the job surprisingly 
  easy, '
                'and the duo begins to make big money. But at what price? With '
                'wealth and prosperity a driving daily goal for Lily, will her '
                'own family come to bear the cost? Director Lee Lok See 
  uses his '
                'Shanghai focus to great effect, finding many avenues and '
                'opportunities for his satirical observations and cultural '
                'clashes. With capitalism and communism going head on in the '
                'rapidly growing city of Shanghai, which value system will '
                "ultimately live in each person's heart?",
    'popularity': 0.93,
    'poster_path': '/5mCwVOIU5LNbGKsDy7n12w0ZqQj.jpg',
    'release_date': '1994-05-12',
    'title': 'Shanghai Fever',
    'video': False,
    'vote_average': 7.3,
    'vote_count': 3},
  {'adult': False,
    'backdrop_path': '/ydmZIafp66mHABs3QJDwvjRgZfE.jpg',
    'genre_ids': [18, 28, 36],
    'id': 359724,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': 'Ford v Ferrari',
    'overview': '1960년대, 매출 감소에 빠진 포드는 판매 활로를 찾기 위해
  페라리와의 인수 합병을 추진한다. 막대한 자금력에도 '
                '불구, 계약에 실패하고 엔초 페라리로부터 모욕까지 당한  
  헨리 포드 2세는 르망 24시간 레이스에서 페라리를 박살 '
                '낼 차를 만들 것을 지시한다. 지옥의 레이스로 불리는 르망
  24시간 레이스. 출전 경험조차 없는 포드는 대회 '
                '6연패를 차지한 페라리에 대항하기 위해 르망 우승자 출신 
  자동차 디자이너 캐롤 셸비를 고용하고, 그는 누구와도 '
                '타협하지 않지만 열정과 실력만큼은 최고인 레이서 켄 마일
  스를 자신의 파트너로 영입하는데...',
    'popularity': 44.241,
    'poster_path': '/wBUoWL4z0nsvC9cYT3VCc74X3jE.jpg',
    'release_date': '2019-11-13',
    'title': '포드 V 페라리',
    'video': False,
    'vote_average': 8.007,
    'vote_count': 6350},
  {'adult': False,
    'backdrop_path': '/dIWwZW7dJJtqC6CgWzYkNVKIUm8.jpg',
    'genre_ids': [10749, 16, 18],
    'id': 372058,
    'media_type': 'movie',
    'original_language': 'ja',
    'original_title': '君の名は。',
    'overview': '시골에 사는 소녀 미츠하(가미시라이시 모네)는 어느 날 잠
  에서 깬 후 자신의 몸이 남자로 바뀐 걸 알게 된다. '
                '같은 시간, 도쿄에 사는 소년 타키(가미키 류노스케) 역시 
  이 기이한 상황을 겪고 있다. 낯선 가족, 낯선 '
                '친구들, 낯선 풍경들... 서로에게 이어진 끈을 알게 된 둘 
  은 둘만의 규칙을 정하고 점차 상황을 받아들이기 '
                '시작한다. 서로에게 남긴 메모를 확인하며  점점 친구가 되
  어가는 타키와 미츠하. 언제부턴가 더 이상 몸이 바뀌지 '
                '않자  자신들이 특별하게 이어져있었음을 깨달은  타키는  
  미츠하를 만나러 가는데...',
    'popularity': 94.206,
    'poster_path': '/wx1Dxr4UyvN18SyC5GsVWWWtYja.jpg',
    'release_date': '2016-08-26',
    'title': '너의 이름은',
    'video': False,
    'vote_average': 8.519,
    'vote_count': 9436},
  {'adult': False,
    'backdrop_path': '/wPU78OPN4BYEgWYdXyg0phMee64.jpg',
    'genre_ids': [18, 80],
    'id': 278,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': 'The Shawshank Redemption',
    'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를
  살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
                '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수 
  용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
                '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 
  짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
                '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 
  회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
                '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 
  세탁하여 불려주면서 그의 돈을 관리하는데...',
    'popularity': 84.949,
    'poster_path': '/oAt6OtpwYCdJI76AVtVKW1eorYx.jpg',
    'release_date': '1994-09-23',
    'title': '쇼생크 탈출',
    'video': False,
    'vote_average': 8.7,
    'vote_count': 23156},
  {'adult': False,
    'backdrop_path': None,
    'genre_ids': [],
    'id': 514238,
    'media_type': 'movie',
    'original_language': 'ar',
    'original_title': 'سومياتي بتدخل النار ؟',
    'overview': 'A seven-year-old child narrates the struggles of her nanny, '
                'Sumyati, who must navigate prejudice and cruel treatment from '
                'the family she works for.',
    'popularity': 1.666,
    'poster_path': '/sj72feR0YFz8b4rymUyCVGgZDeN.jpg',
    'release_date': '2016-11-03',
    'title': 'Is Sumiyati Going to Hell?',
    'video': False,
    'vote_average': 7.7,
    'vote_count': 6},
  {'adult': False,
    'backdrop_path': '/sOJqNAx4RFrCRn8HS99LEc8aenI.jpg',
    'genre_ids': [18, 10749, 36],
    'id': 331482,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': 'Little Women',
    'overview': '첫째 메그는 배우가 되고 싶은 욕망과 가족을 가지고 싶어 
  하는 욕망 사이에서 고민하고, 둘째 조는 소설을 쓰지만 '
                '여성들이 쓴 소설은 어떻게 끝이 나야 하는지 잘 알고 있는
  척하는 편집장과 맞서야 한다. 셋째 베스는 피아노를 잘 '
                '치지만 건강에 문제가 있고, 막내 에이미는 그림을 그리는 
  데 소질이 있지만 남자들이 좋아하는 취향에 따라 그림을 '
                '그려야 하는 상황에 처한다. 이웃집 소년 로리는 네 자매를
  우연히 알게 되고, 각기 다른 개성의 네 자매들과 '
                '인연을 쌓아 간다. 7년 후, 어른이 된 그들에겐 각기 다른 
  숙제가 놓이게 되는데...',
    'popularity': 38.46,
    'poster_path': '/2kfDJEwZ7Rxo3yz5v6rJlwqtY0W.jpg',
    'release_date': '2019-12-25',
    'title': '작은 아씨들',
    'video': False,
    'vote_average': 7.904,
    'vote_count': 5277},
  {'adult': False,
    'backdrop_path': '/suaEOtk1N1sgg2MTM7oZd2cfVp3.jpg',
    'genre_ids': [53, 80],
    'id': 680,
    'media_type': 'movie',
    'original_language': 'en',
    'original_title': 'Pulp Fiction',
    'overview': '펌프킨와 허니 버니가 레스토랑에서 강도 행각을 벌이기 시
  작한다. 빈센트와 그 동료 쥴스는 두목의 금가방을 찾기 '
                '위해 다른 건달이 사는 아파트를 찾아간다. 마르셀러스는  
  부치에게 돈을 주며 상대 선수에게 져 주라고 하지만 부치는 '
                '상대 선수를 때려 눕히고 도망치다, 어릴 때 아버지에게 물
  려받은 시계를 찾기 위해 아파트로 향한다. 아무런 상관 '
                '없이 보이는 이 사건들이 서로 얽히고 섥히면서 예상치 못 
  한 인과관계가 만들어지는데...',
    'popularity': 57.231,
    'poster_path': '/6lXRHGoEbnnBUKsuqpL9JxD4DzT.jpg',
    'release_date': '1994-09-10',
    'title': '펄프 픽션',
    'video': False,
    'vote_average': 8.49,
    'vote_count': 24523}]
  []
  None
  
  * 문제 접근 방법 및 코드 설명
    * url과 parameter을 이용하여 불러온 후 원하는 데이터를 추출하고, 추출한 데이터를 기반으로 새로운 데이터를 불러와 return
  
```python
def recommendation(title):

    URL = f'https://api.themoviedb.org/3/search/movie'
    
    param= {
        'api_key' : '6a5ece7778e61cb35c55c953b8743b0d',
        'language' : 'ko-KR',
        'region' : 'KR',
        'query' : title,
        'page' : 1
    }
    
    r = requests.get(URL, params = param).json().get('results')

    
    
    if not r:
        return None

    else:
        ids = r[0]['id']
    
    
    recom_URL = f'https://api.themoviedb.org/3/movie/{ids}/recommendations'

    recom_URL_param = {
        'api_key' : '6a5ece7778e61cb35c55c953b8743b0d',
        'language' : 'ko-KR',
        'region' : 'KR',
    }
    
    recom_movie = requests.get(recom_URL, params = recom_URL_param).json().get('results')


    if not recom_movie :
        return []

    else:
        return recom_movie
```
  
  * 이 문제에서 어려웠던점
    * requests의 사용, 조건 설정
  * 내가 생각하는 이 문제의 포인트
    * requests 사용법 / 조건에 따른 반환값 설정(None, [])

## E. 출연진, 연출진 데이터 조회

* 요구 사항 : 제공된 영화 제목을 검색하여 해당 영화의 출연진과 스태프 중 연출진의 이름을 출력

* 결과 : 
  {'cast': ['Song Kang-ho',
            'Lee Sun-kyun',
            'Cho Yeo-jeong',
            'Choi Woo-shik',
            'Park So-dam',
            'Lee Jung-eun',
            'Jang Hye-jin'],
  'directing': ['Bong Joon-ho',
                'Park Hyun-cheol',
                'Han Jin-won',
                'Kim Seong-sik',
                'Lee Jung-hoon',
                'Yoon Young-woo']}
  None
  
  * 문제 접근 방법 및 코드 설명
    * url과 parameter을 이용하여 불러오고 결과값의 길이를 return
  
```python
import requests
from pprint import pprint

def credits(title):

    URL = f'https://api.themoviedb.org/3/search/movie'
    
    param= {
        'api_key' : '6a5ece7778e61cb35c55c953b8743b0d',
        'language' : 'ko-KR',
        'region' : 'KR',
        'query' : title,
        'page' : 1
    }
    
    r = requests.get(URL, params = param).json().get('results')

    if not r:
        return None

    else:
        ids = r[0]['id']

    credit_URL = f'https://api.themoviedb.org/3/movie/{ids}/credits'

    credit_URL_param = {
        'api_key' : '6a5ece7778e61cb35c55c953b8743b0d',
        'language' : 'ko-KR',
        'region' : 'KR',
    }

    credit_movie = requests.get(credit_URL, params = credit_URL_param).json()
    
    credit_movie_cast = credit_movie['cast']
    credit_movie_crew = credit_movie['crew']    

    cast_dic = {
        'cast' : [],
        'directing' : []
    }
    for cr in credit_movie_crew:
        if cr['department'] == 'Directing':
            cast_dic['directing'] += [cr['name']]

    for ca in credit_movie_cast:
        if ca['known_for_department'] == 'Acting':
            if ca['cast_id'] < 10:
                cast_dic['cast'] += [ca['name']]

    return cast_dic
```
  
  * 이 문제에서 어려웠던점
    * 문제를 제대로 안봐서 crew가 따로 있는 지 몰랐음.
  * 내가 생각하는 이 문제의 포인트
    * requests 사용법, for문과 if문을 통한 조건 설정






-----

....

문제 푼 내용을 기반으로 적어주세요.

# 후기

* 홈페이지에서 open api를 이용하여 데이터를 추출하고 활용하는 연습을 처음 경험해보았는데 재밌었습니다. 요즘은 open api를 얼마나 잘 이용하는 지가 더욱 중요해지는 시대라고 교수님께서 강조하셨기 때문에 집중해서 참여했던 pjt였습니다.
