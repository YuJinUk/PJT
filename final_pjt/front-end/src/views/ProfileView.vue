<template>
  <div class="background">
    <h1 style="color: white;"> {{ username }} 님의 Profile</h1>
    <div style="background-color: lightblue; margin:auto; width:50%; color: black; border-radius:20px;">
    <p style="font-weight: bolder; margin-bottom: 0px;">
        my email
    </p>
    <hr>
    <p style="margin-top: 0px; margin-bottom: 0px;">
        {{ email }}
    </p>
    </div>
    <!-- <br> -->
    <!-- <div style="background-color: lightblue; margin:auto; width:50%; color: black; border-radius:20px;">
        <p style="font-weight: bolder;">
            내가 좋아하는 장르
        </p>
        <p style="color: white">{{ genre }}</p>
    </div> -->
    <br>
    <!-- 사용자 닉네임 : {{ nickname }} -->
    <router-link to="/profileChange">
    <div style="background-color: lightblue; margin:auto; width:50%; color: black; border-radius:20px;">
    비밀번호 변경
    </div>
    <br>
    </router-link>
    <div style="background-color: lightblue; margin:auto; width:50%; color: black; border-radius:20px;">
        좋아요 누른 영화
    </div>
    <carousel :per-page="5" :paginationEnabled="true">
    <slide
    v-for="(like_movie, idx) in like_movies" :key="idx"
    >
    <!-- <p>2번째</p> -->
    <!-- {{ like_movie }} -->
    <div class="card" @click="reload()">
        <router-link :to="{
          name: 'DetailView',
          params: {id: like_movie.movie_id }}">
          <div class="card h-100">
          <img :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2/${like_movie?.poster_path}`" class="mx-5 w-75 rounded">
          </div>
        </router-link>
    </div>
    </slide>
    </carousel>
    <br>
    <ul v-if="like_movies!==null">
    <MovieRecommendProfile v-bind:like_movies="like_movies"/>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import MovieRecommendProfile from '@/components/MovieRecommendProfile.vue'
import { Carousel, Slide } from 'vue-carousel';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',

  components: {
    MovieRecommendProfile,
    Carousel,
    Slide,
  },

  data() {
    return {
      user: null,   
      username: null,
      email: null,
      genre: 'Actions',
      like_movies: [],
    }
  },
  created() {
    this.getUser()
    
  },
  methods: {
    getUser() {
      const token = this.$store.state.token
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
        Authorization: `Token ${token}`
        }
      })
      .then((res) => {
        console.log(res.data)
        this.user = res.data
        this.username = res.data.username
        this.email = res.data.email
        // this.nickname = res.data.nickname
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/users/${this.username}`,
          headers: {
          Authorization: `Token ${token}`
          }
        })
          .then((res) => {
            console.log(res.data)
            console.log('checkcheckcheckcheckcheckcheck')
        //   console.log(res.data.like_movies)
            // console.log('checkcheckcheckcheckcheckcheck')
          this.like_movies = res.data.like_movies
          this.genre = res.data.genres
          // this.nickname = res.data.nickname
          })
          .catch((err) => {
            console.log(err)
          })
        })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}
</script>

<style>
.background {
  height: 200vh;
  width: 100vw;
  background-color: #141414
}
</style>