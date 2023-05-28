<template>
  <div class="backgroud my-component d-flex flex-column mb-3" :style="`background-image: url(${movie?.backdrop_path})`">
    <h1 style="margin: auto; width: 40%; background-color:white; color: black; padding:20px; border-radius:20px;">
        {{ movie?.eng_title }}
    </h1>
    <div class="d-flex" style="padding: 40px"> 
        <!-- 1번째 틀 -->
    <div style="margin-top: 50px; width: 50%">
    <!-- <img style="height: 600px" :src="`${ movie?.backdrop_path }`" alt="" srcset=""> -->
    <img style="height: 1000px; border-radius:20px;" :src="`${ movie?.poster_path }`" alt="" srcset="">
    </div>
    <div style="margin-top: 50px; width: 50%; background-color:white; color: black; padding:20px; border-radius:20px;">
    <div style="background-color: lightblue; color: black; border-radius:20px;">
    <p style="font-weight: bolder">한국어 제목 : {{ movie?.title }}</p>
    </div>
    <div style="background-color: lightblue; color: black; border-radius:20px;">
    <p>어떤 장르인가요?</p>
    <div>
        <span style="margin: auto" v-for="(gen, ids) in movie?.genres" :key="ids">
            <button type="button" class="btn btn-primary" disabled>
                {{ gen.genre_ids }}
            </button>
            &nbsp;
        </span>
    </div>
    </div>
    <br>
    <div style="background-color: lightblue; color: black; border-radius:20px;">
    <p>청소년은?</p>
    <div v-if="movie?.adult">
        못봐요
    </div>
    <div v-else>
        볼 수 있어요
    </div>
    </div>
    <br>
    <div style="background-color: lightblue; color: black; border-radius:20px;">
    <p> 이 영화를 본 사람들의 평가는? </p>
        {{ movie?.vote_average }}
    </div>
    <br>
    <div style="background-color: lightblue; color: black; border-radius:20px;">
    <p> 이 영화를 본 전문가들의 평가는? </p>
        {{ movie?.popularity }}
    </div>
    <br>
    <div style="background-color: lightblue; color: black; border-radius:20px;">
    <p> 언제 개봉했나요? </p>
        {{ movie?.release_date }}
    </div>
    <br>
    <div style="background-color: lightblue; color: black; border-radius:20px;">
    <button type="button" class="btn btn-primary" disabled> 줄거리 </button>
    <br>
    <div type="button" class="btn" disabled>
    {{ movie?.overview }}
    </div>
    </div>
    <br>
    <div style="background-color: lightblue; color: black; border-radius:20px;">
        공식 영상 보러가기
        <br><br>
        <span style="margin: auto" v-for="(vid, idx) in movie?.videos" :key="idx">
            <!-- {{vid.video}} -->
            <button type="button" class="btn btn-primary" :onclick="`window.open('${vid.video}')`" style="color: white;">
                관련 공식 영상 {{ idx + 1 }}
            </button>
            &nbsp;
        </span>
    </div>
    <br>
    <div style="background-color: lightblue; color: black; border-radius:20px;">
    <li style="list-style: none;" v-if="movie?.like_users.indexOf(user.pk) !== -1">
        <p>{{movie?.user}} 님이 좋아하는 영화입니다.</p>
        <button type="button" class="btn btn-outline-secondary" @click="getlikes()">좋아요 취소</button>
    </li>
    <li v-else style="list-style-type: none;"> 
        <p>영화에 관심이 있다면 아래 버튼을 눌러보세요</p>
        <button type="button" class="btn btn-outline-secondary" @click="getlikes()">좋아요</button>
    </li>
    </div>
    </div>
    <!-- </button> -->
    <!-- <br><br> -->
    <br>
    </div>
    <div>
    <MovieComments/>
    </div>
    <br><br>
    <div>
    <ul v-if="movie !== null">
        <MovieRecommend v-bind:movie="movie"/>
    </ul>
    </div>
    <br>
    
    <!-- <MovieCommentsList/> -->
  </div>
</template>

<script>
import axios from 'axios'
import MovieRecommend from '@/components/MovieRecommend.vue'
import MovieComments from '@/components/MovieComments.vue'
// import MovieCommentsList from '@/components/MovieCommentsList.vue'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components: {
    MovieRecommend, MovieComments
  },

  data() {
    return {
      // allmovie: this.$store.state.movie,
      movie: null,
      user: this.$store.state.user,
      username: this.$store.state.username,
      email: this.$store.state.email,
    }
  },
  created() {
    // console.log(this.user)
    // console.log('유저 네임 확인용')
    this.getUser(),
    this.getMovieDetail()
    // console.allmovie
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${ this.$route.params.id }`,
      })
      .then((res) => {
        // console.log(res.data)
        this.movie = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getUser() {
      this.$store.dispatch('getUser')
      
    },
    getlikes() {
      console.log(this.$route.params.id)
      const movie_id = this.$route.params.id
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${ this.$route.params.id }/likes/`,
        data:{
          movie_id
        },
        headers:{
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.movie = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
/* .my-component {
  background-image: url();
  background-repeat: no-repeat;
  background-size: cover;
} */
.background {
    height: 100vh;
  width: 100vw;
  background-color: #141414
}
.my-component {
    background-repeat: no-repeat;
    background-size: 150vw;
}
</style>