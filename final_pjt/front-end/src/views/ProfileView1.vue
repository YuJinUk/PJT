<template>
  <div>
    <h1>Profile</h1>
		{{user}}
    사용자명 : {{ username }}
    <br>
    사용자 이메일 : {{ email }}
    <br>
		{{nickname}}
		{{genres}}
    <!-- 사용자 닉네임 : {{ nickname }} -->
		<div class="row row-cols-1 row-cols-md-5 g-4">
    <div
    v-for="like_movie in like_movies" :key="like_movie.id" :movie="movie"
    >
    <div class="card">
      
        <router-link :to="{
          name: 'DetailView',
          params: {id: like_movie.movie_id }}">
          <div class="card h-100">
          <img :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2/${like_movie.poster_path}`" alt="" srcset="">
          
          </div>
        </router-link>
      
    </div>
    </div>
    </div>
    <router-link to="/profilechange">changepassword</router-link>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
			like_movies: [],
      user: null,
      username: null,
			// nickname: null,
      email: null,
			profile_img: null,
      genres: null
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
        url: `${API_URL}/users/${ this.$store.state.usernamne }`,
        headers: {
        Authorization: `Token ${token}`
        }
      })
      .then((res) => {
        // console.log(token)
        this.user = res.data
        this.username = res.data.username
        // this.nickname = res.data.nickname
				this.email = res.data.email
				this.profile_img = res.data.profile_img
        this.genres = res.data.genres
				this.like_movies = res.data.like_movies
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>
