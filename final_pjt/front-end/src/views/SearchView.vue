<template>
    <div class="background">
        <br><br>
      <h1 style="color: white;">Search list</h1>
      <hr>
      <!-- adult, backdrop_path, genre_ids, id, original_language,...  -->
      <ul class="scroll-container">
        <br><br>
            <div id="new_container" class="row row-cols-1 row-cols-md-6 g-4">
                <div v-for="(search_movie, idx) in this.search_movies" :key="idx" style="margin-bottom: 20px;">
                <div class="col card-custom-back">
                <!-- <div class="card card-custom-back" style="width: 100px;"> -->
                <!-- <div class="card-custom-back"> -->
                    <router-link :to="{
                            name: 'DetailView',
                            params: {id: search_movie.id }}">
                            <img class="card-custom p-3" :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2/${search_movie.poster_path}`" style="border-radius: 20%;">
                        </router-link>
                    <div class="card-body" style="margin: 0px; padding: 0px;">
                        <span class="card-title">
                            <button type="button" class="btn btn-outline-dark" style="width: 180px ;margin-top: 10px; margin-bottom: 5px; color: black;">
                                {{ search_movie.title }}
                            </button>
                        </span>
                        <br>
            </div>
        <!-- </div> -->
    <!-- </div> -->
</div>
</div>
</div>
</ul>
<!-- <div v-for="search_movie in this.search_movies" :key="search_movie.id" :search_movie="search_movie">
    <p><img :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2/${search_movie.poster_path}`" alt="" srcset=""></p>
    <p>{{ search_movie.title }}</p>
    <p></p>
    <p>{{ search_movie.vote_average }}</p>
    <router-link :to="{
    name: 'DetailView',
    params: {id: search_movie.id }}">
    DETAIL
    </router-link>
</div> -->
</div>
</template>
  
  <script>
  export default {
    name: 'SearchView',
    data(){
        return {
            search_movies: this.$store.state.search_movies
        }
    },
    components: {
    },
    computed:{
      isLogin() {
        return this.$store.getters.isLogin // 로그인 여부
      }
    },
    created() {
      this.getSearchMovies()
    },
    methods: {
      getSearchMovies() {
        if (this.isLogin) {
            // console.log(this.$store.state.search_movies)
          // this.$store.dispatch('getSearchMovies')
        } else {
          alert('로그인이 필요한 페이지입니다...')
        }
  
  
        // 로그인이 되어 있으면 getArticles action 실행
        // 로그인 X라면 login 페이지로 이동
  
      },

    }
  }
  </script>
  
  <style>
  .container {
    display: flex;
    align-items: center;
    justify-content: center;
    /* height: 100vh; */
  }
  
  .box {
    font-weight: bold;
    background-color: black;
    color: white;
    height: 50px;
    width: 60%;
  }
  .scroll_container {
    width: 100%;
    overflow-x: scroll;
    white-space: nowrap;
  }
  
  #new_container {
    height: 500px;
    overflow: auto;
  }
  ::-webkit-scrollbar {
    width: 10px;
    height: 20px;
  }
  ::-webkit-scrollbar-thumb {
    /* background: 스크롤바 막대 색상 black; */
    border-radius: 10%;
  }
  .card-custom {
    /* 원하는 카드 크기로 조정 */
    width: 100px;
    height: 150px;
    margin: 50px;
  }
  .card-custom-back {
    /* 원하는 카드 크기로 조정 */
    width: 210px;
    height: 380px;
    margin: 50px;
    border-radius: 20px;
    background-color: rgb(241, 240, 240);
  }
.background {
  height: 200vh;
  width: 100vw;
  background-color: #141414
}
  </style>
  