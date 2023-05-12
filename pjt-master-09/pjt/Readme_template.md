# PJT 01

### 이번 pjt 를 통해 배운 내용

* Vue가 할 수 있는 역할이 정말 많다는 것을 깨달았다

* 프론트는 같은 것을 위해 할 수 있는 방법이 다양하다

## A. 최고 평점 영화 출력

* 요구 사항 : 네비게이션 바에서 Movie 링크(/movies)를 클릭하면 AJAX 통신을 이용하여      TMDB API로 부터 JSON 데이터를 받아와 다음과 같이 영화 목록을 출력합니다

* 결과 : API를 통해 영화 데이터를 받아 URL로 사진을 출력했습니다.
  
  * 문제 접근 방법 및 코드 설명
  
  ```javascript
  <template>
    <div class="container-sm">
    <div class="row row-cols-1 row-cols-md-2 g-4">
      <ul v-for="mov in m_list" :key="mov.title">
      <div class="card-group h-100">
          <div class="card">
              <img :src="getImageURL(mov.poster_path)" class="card-img-top" alt="">
              <div class="card-body">
              <h5 class="card-title">{{mov.title}}</h5>
              <p class="card-text">{{mov.overview}}</p>
              </div>
          </div>
      </div>
      </ul>
    </div>
    </div>
  </template>
  
  <script>
  
  import axios from 'axios'
  const Movie_URL = 'https://api.themoviedb.org/3/movie/top_rated?'
  const Movie_API = '6a5ece7778e61cb35c55c953b8743b0d'
  
  export default {
      name: 'MovieView',
      data() {
          return {
              m_list: null,
          }
      },
      computed: {
  
      },
      methods: {
          getMovieImg() {
              const getMovieURL = Movie_URL
              const getMovieAPI = Movie_API
              // const getPictureURL = Picture_URL
  
              axios({
                  method: 'get',
                  url: `${getMovieURL}api_key=${getMovieAPI}`
              })
              .then((res) => {
                  // console.log('일단 response')
                  console.log(res.data.results)
                  this.m_list = res.data.results
              })
              .catch((err) => {
                  console.log(err)
              })
          },
          getImageURL(posterPath) {
          if (posterPath) {
              console.log('포스터패스 들어감')
              return `https://image.tmdb.org/t/p/w500${posterPath}`
          }
          return '' // 이미지가 없을 경우에 대한 처리
          },
      },
      created() {
          this.getMovieImg()
      }
  }
  </script>
  
  <style>
  
  </style>
  ```
  
  * 이 문제에서 어려웠던점
    * URL 및 API_KEY를 통해 정보를 받아온 것을 기반으로 또 다시 URL을 통해 Image를 출력해줘야하여 여러번 반복하는 것이 쉽지 않았습니다.
  * 내가 생각하는 이 문제의 포인트
    * URL 및 API_KEY를 잘 이용하는 것

## B. 최고 평점 영화 중 랜덤 영화 한 개 출력

- 요구 사항 : 네비게이션 바에서 Random 링크(/random)를 클릭하면 저장된 최고 평점 영화 목록 중 랜덤으로 한 개를 출력합니다

- 결과 : 기존 데이터에서 랜덤하게 뽑아 영화의 포스터와 제목을 출력했습니다.
  
  - 문제 접근 방법 및 코드 설명
  
  ```javascript
  <template>
    <div>
      <button @click="getMovieImg">New Recommand</button>
      <br><br>
      <img :src="getImageURL(random_movie.poster_path)" alt="">
      <br>
      <h2>{{random_movie.title}}</h2>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  const Movie_URL = 'https://api.themoviedb.org/3/movie/top_rated?'
  const Movie_API = '6a5ece7778e61cb35c55c953b8743b0d'
  
  export default {
      name: 'RandomView',
      data() {
          return {
              m_list: null,
              m_length: 0,
              random_num: 0,
              random_movie: 0,
          }
      },
      computed: {
  
      },
      methods: {
          getMovieImg() {
              const getMovieURL = Movie_URL
              const getMovieAPI = Movie_API
  
              axios({
                  method: 'get',
                  url: `${getMovieURL}api_key=${getMovieAPI}`
              })
              .then((res) => {
                  // console.log('일단 response')
                  // console.log(res.data.results)
                  this.m_list = res.data.results
                  this.m_length = this.m_list.length
                  // console.log(this.m_length)
                  this.random_num = Math.ceil(Math.random() * (this.m_length-1))
                  // console.log(this.random_num)
                  this.random_movie = this.m_list[this.random_num]
                  // console.log(this.random_movie)
                  
              })
              .catch((err) => {
                  console.log(err)
              })
          },
          getImageURL(posterPath) {
          if (posterPath) {
              console.log('포스터패스 들어감')
              return `https://image.tmdb.org/t/p/w500${posterPath}`
          }
          return '' // 이미지가 없을 경우에 대한 처리
          },
      },
      created() {
          this.getMovieImg()
      }
  }
  </script>
  
  <style>
  
  </style>
  ```
  
  - 이 문제에서 어려웠던점
    - python과는 다른 문법으로 갖고있는 영화의 총 개수를 가져와 0과 총 개수 사이의 random number을 뽑아 index를 매칭시켜 영화를 뽑아내는 것이 어려웠습니다.
  - 내가 생각하는 이 문제의 포인트
    - 랜덤한 숫자를 뽑아내는 것과 v-for을 활용하여 index를 methods에 보내주는 것이 중요합니다.

## C. 보고 싶은 영화 등록 및 삭제하기

- 요구 사항 : 네비게이션 바에서 WatchList 링크(/watch-list)를 클릭하면 보고 싶은 영화 제목을 등록할 수 있는 Form이 출력됩니다. / 등록된 영화 제목을 클릭하면 취소선이 그어집니다.

- 결과 : 입력하여 엔터 or Add버튼을 누를 때 데이터를 list에 추가하여 v-for을 통해 출력하게 해주었으며 v-bind:class를 활용하여 한번 누르면 취소선을, 두번 누르면 취소선이 사라지도록 만들었습니다.
  
  - 문제 접근 방법 및 코드 설명
  
  ```javascript
  <template>
    <div>
      <h1>보고싶은 영화</h1>
      <div>
      <input type="text" v-model="want_movie" @keyup.enter="addMovie()">
      <button @click="addMovie()">Add</button>
      </div>
      <br><br>
      <div>
          <ul v-for="(check_list, index) in want_movie_list" :key="index">
              <li>
                  <button :class="{'strike-through' : check_list.is_completed}" style="border:None; background-color:white;" @click="deleteMovie(index)">{{check_list.want_movie_value}}</button>
              </li>
          </ul>
      </div>
    </div>
  </template>
  
  <script>
  
  export default {
      name : 'WatchList',
      data() {
          return {
              want_movie: null,
              want_movie_list: [],
              movie_idx: null,
              line_list: [],
          }
      },
      methods: {
          addMovie() {
              // console.log(want_movie_value)
              const want_movie_value = this.want_movie
              if (want_movie_value != null) {
                  this.want_movie_list.push({want_movie_value, is_completed : false})
                  console.log(this.want_movie_list)
                  this.want_movie = null
              } else {
                  this.want_movie = null
              }
  
          },
          deleteMovie(idx) {
              const movielist = this.want_movie_list
              // console.log(movielist)
              // console.log(idx)
              const movieindex = idx
              // console.log(movielist[movieindex].is_completed)
              movielist[movieindex].is_completed = !movielist[movieindex].is_completed
  
              // movielist.splice(movieindex, 1)
              // console.log(movielist)
              // this.want_movie_list = movielist
          }
      },
  }
  </script>
  
  <style>
  .strike-through {
      text-decoration: line-through;
  }
  </style>
  ```
  
  - 이 문제에서 어려웠던점
    - 데이터를 추가하면서 true, false를 변환시켜주는 과정이 생각하는 과정에서 가장 어려웠습니다.
  - 내가 생각하는 이 문제의 포인트
    - true, false를 자유자재로 변환하기

-----

....

문제 푼 내용을 기반으로 적어주세요.

# 후기

* Vue는 프론트지만 생각보다 백엔드와 가까운 것 같습니다.
* 어쩌면 프론트에서 할 수 있는 것이 생각보다 많을 것이라고 생각이 듭니다.
* methods, data, html사이의 연결 관계를 파악하고 데이터를 불러오거나 함수를 호출하는 것이 정말 중요하다는 것을 느꼈습니다.
* vuex를 통해 데이터를 store에 저장할 수 있는 방법도 있지만 금일 진행하는 프로젝트에서는 복잡함이 상대적으로 적어 vuex를 사용하지 않았지만 구현해야하는 프로젝트가 복잡하다면 vuex를 통해 store에서 데이터를 주고받는 과정이 더 편리하며 코드 복잡도도 줄일 수 있을 것이라고 생각합니다.
* 어떤 프로젝트냐에 따라 정말 다양한 코드구현이 가능하다고 생각합니다.
