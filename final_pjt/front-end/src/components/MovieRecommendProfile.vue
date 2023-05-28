<template>
	<div>
    <h1 style="color: white;">추천 영화</h1>
    <button type="button" class="btn btn-primary" @click="recommendMovies()">눌러봐</button>
    <carousel :per-page="5" :paginationEnabled="true">
    <slide
    v-for="(recommend_movie, idx) in recommend_movies" :key="idx"
    >

    <div class="card" @click="reload()">
      
        <router-link :to="{
          name: 'DetailView',
          params: {id: recommend_movie.movie_id }}">
          <div class="card h-100">
          <img :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2/${recommend_movie.poster_path}`" class="mx-5 w-75 rounded">
          </div>
        </router-link>
      
    </div>
    </slide>
    </carousel>
  </div>
</template>

<script>
import axios from 'axios'
import { Carousel, Slide } from 'vue-carousel';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieRecommendProfile',
  components: {
    Carousel,
    Slide,
  },
  props: {
    like_movies: Array,
  },
  data() {
    return {
      recommend_movies: [],
      like_movie: null,
    }
  },
  computed: {
    // like_movies_computed() {
    //    return this.like_movies
    },
//   created(){
//     this.recommendMovies()
//   },
  methods: {
    recommendMovies(){
    //   console.log(this.like_movies)
    //   console.log('일단 like_movie확인')
      const movie_title = this.like_movies
      console.log('---------------------')
      console.log(movie_title)
      console.log('---------------------')
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/recommends/profile/`,
        data: {
          movie: movie_title
        }
      })
      .then((res) => {
        // console.log(res)
        // console.log(res.data)
        this.recommend_movies = res.data
        console.log(this.recommend_movies)

      })
      .catch((err) => {
        console.log(err)
      })
    },
    reload() {
      location.reload(true)
    }
  }
}
</script>