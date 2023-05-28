<template>
	<div>
    <div style="margin: auto; width: 100%; background-color:white; color: black; padding:20px; border-radius:20px;">
    <h1>MovieRecommend</h1>
    </div>
    <!-- <div class="row row-cols-1 row-cols-md-5 g-4"> -->
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
    <!-- </div> -->
  </div>
</template>

<script>
import axios from 'axios'
import { Carousel, Slide } from 'vue-carousel';
// import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieRecommend',
  components: {
    Carousel,
    Slide
  },
  data() {
    return {
      recommend_movies: [],
    }
  },
  props: {
    movie: Object,
  },
  created(){
    this.recommendMovies()
  },
  // mounted() {
  //   this.startCursor()
  // },
  methods: {
    recommendMovies(){
      const movie_title = this.movie?.title
      // console.log(movie_title)

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/recommends/`,
        data: {
          movie: movie_title
        }
      })
      .then((res) => {
        // console.log(res)
        // console.log(res.data)
        this.recommend_movies = res.data
        // console.log(this.recommend_movies)

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