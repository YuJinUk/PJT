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
// const Picture_URL = 'https://image.tmdb.org/t/p/w500'

export default {
    name: 'RandomView',
    data() {
        return {
            m_list: null,
            m_length: 0,
            random_num: 0,
            random_movie: 0,
            // image: null,
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