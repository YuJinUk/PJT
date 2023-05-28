<template>
  <div class="">
    <br><br>
    <h3 class="text-light">Best Movie</h3>

		<br><br>
		<div class="row row-cols-1 row-cols-md-5 g-4">
    <div v-for="movie in AllBestMovies" :key="movie.id" :movie="movie">
			<!-- {{movie.title}} -->
			<router-link :to="{
      name: 'DetailView',
      params: {id: movie.movie_id }}">
			<div class="col">
        <div class="card h-100">
            <img :src="`https://image.tmdb.org/t/p/w220_and_h330_face/${movie.poster_path}`" class="card-img-top" alt="" srcset="">
            <!-- <div class="card-body h-100">
                <h5 class="card-title">
                    {{ movie.title }}
                </h5>
                <p class="card-text">
                    {{ movie.overview }}
                </p>
            </div> -->
        </div>
        </div>
      </router-link>
		</div>
		</div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieBestList',

	data() {
		return {
			AllBestMovies:null
		}
	},
  computed: {
    // Todaymovies() {
    //   return this.$store.state.today_movies
    // }
  },
	created() {
      this.BestMovie()
    },

	methods: {
		BestMovie() {
			axios({
				method: 'get',
				url: `${API_URL}/api/v1/movies/`,
			})
			.then((res) => {
				console.log(res.data)
				this.AllBestMovies = res.data
      })
      .catch((err) => {
      console.log(err)
      })
		}
	}
}
</script>

<style>

</style>
