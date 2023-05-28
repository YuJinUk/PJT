<template>
  <div class="">
    <br><br>
    <h3 class="text-light" style="color: white;">AllMovie</h3>
	<br>
    <br>
		<div class="">

			<div class="btn-group" role="group" aria-label="Button group with nested dropdown">
			<button type="button" class="btn btn-dark" @click="result(page=1)"> first </button>
			<button type="button" class="btn btn-dark" @click="unitdown(page-10)"> &lt;&lt; </button>
			<button type="button" class="btn btn-dark" v-if="page==486" @click="result(page-2)"> {{ page-2 }} </button>
			<button type="button" class="btn btn-dark" v-if="page!=1 & page-1!=486" @click="result(page-1)"> {{ page-1 }} </button>
			<!-- <button v-if="page-1!=486" @click="result(page-1)"> {{ page-1 }} </button> -->
			<button type="button" class="btn btn-dark" @click="result(page)"> {{ page }}</button>
			<button type="button" class="btn btn-dark" v-if="page!=486" @click="result(page+1)"> {{ page+1 }}</button>
			<button type="button" class="btn btn-dark" v-if="page==1" @click="result(page+2)"> {{ page+2 }} </button>
			<button type="button" class="btn btn-dark" @click="unitup(page+10)"> &gt;&gt; </button>
			<button type="button" class="btn btn-dark" @click="result(page=486)"> end </button>
			<input class="form-control btn btn-dark" type="search" :placeholder="`현재페이지:   ${page}`" aria-label="Search" v-model.number="new_page" @keyup.enter="result(new_page)">

			<!-- <div class="btn-group" role="group">
				<button type="button" class="btn btn-dark dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
				Dropdown
				</button>
				<ul class="dropdown-menu">
				
				<li><a class="dropdown-item" href="#">Dropdown link</a></li>
				<li><a class="dropdown-item" href="#">Dropdown link</a></li>
				</ul>
			</div> -->
			</div>

		</div>
		<br><br>
		<div class="row row-cols-1 row-cols-md-5 g-4">
    <div v-for="movie in AllMovies" :key="movie.id" :movie="movie">
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
  name: 'MovieList',

	data() {
		return {
			page:1,
			AllMovies:null,
            new_page: null,
		}
	},

  computed: {
    // Todaymovies() {
    //   return this.$store.state.today_movies
    // }
  },
	
  created(){
	this.pagination()
  },
	methods: {
		unitdown(page) {
			if(this.page <= 11){
				this.page=1
			}else{
				this.page=page
			}
			this.pagination()
		},
		unitup(page) {
			if(this.page >= 476){
				this.page=486
			}else{
				this.page=page
			}
			this.pagination()
		},
		result(page) {
			this.page = page
			this.pagination()
		},
		pagination() {
			const page = this.page
			axios({
				method: 'get',
				url: `${API_URL}/api/v1/movies/page=${ page }`,
			})
			.then((res) => {
				console.log(res.data)
				this.AllMovies = res.data
      })
      .catch((err) => {
      console.log(err)
      })
		}
	}
}
</script>

<style>
.form-control::placeholder {
  color: #ffffff;
}
.form-control:-ms-input-placeholder {
  color: #ffffff;
}
</style>
