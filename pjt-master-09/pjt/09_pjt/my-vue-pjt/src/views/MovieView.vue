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
// const Picture_URL = 'https://image.tmdb.org/t/p/w500'

export default {
    name: 'MovieView',
    data() {
        return {
            m_list: null,
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
                console.log(res.data.results)
                this.m_list = res.data.results
            })
            .catch((err) => {
                console.log(err)
            })

            // axios({
            //     method: 'get',
            //     url: `${getPictureURL}${}`
            // })
        },
        getImageURL(posterPath) {
        if (posterPath) {
            console.log('포스터패스 들어감')
            return `https://image.tmdb.org/t/p/w500${posterPath}`
        }
        return '' // 이미지가 없을 경우에 대한 처리
        },
        // getImage(URL) {
        //     const getimgURL = URL

        //     axios({
        //         method: 'get',
        //         url: `${getimgURL}`
        //     })
        //     .then((res) => {
        //         console.log(res)
        //         console.log(getimgURL)
        //         this.image = getimgURL
        //     })
        //     .catch((err) => {
        //         console.log(err)
        //     })
        // }
    },
    created() {
        this.getMovieImg()
    }
}
</script>

<style>

</style>