<template>
  <div class="background">
    <br><br>
    <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
      <input @click="clickBtn(1)" type="radio" class="btn-check" name="btnradio" id="MovieList" autocomplete="off">
      <label class="btn btn-dark" for="MovieList">All Movie</label>

      <input @click="clickBtn(2)" type="radio" class="btn-check" name="btnradio" id="MovieBestList" autocomplete="off" checked>
      <label class="btn btn-dark" for="MovieBestList">Best Movie</label>

      <input @click="clickBtn(3)" type="radio" class="btn-check" name="btnradio" id="MovieTodayList" autocomplete="off">
      <label class="btn btn-dark" for="MovieTodayList">Today Movie</label>
    </div>
    <MovieList v-show="btn==1"/>
    <MovieBestList v-show="btn==2"/>
    <MovieTodayList v-show="btn==3"/>
  </div>
</template>

<script>
import MovieBestList from '@/components/MovieBestList.vue'
import MovieTodayList from '@/components/MovieTodayList.vue'
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'MainView',
  components: {

    MovieBestList,
    MovieList,
    MovieTodayList,

  },
  data() {
    return {
      btn: 2,
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  created() {
    this.getTodayMovies()
  },
  methods: {
    getTodayMovies() {
      if (this.isLogin) {
        this.$store.dispatch('getTodayMovies')
      } else {
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({ name: 'HomeView' })
      }


      // 로그인이 되어 있으면 getArticles action 실행
      // 로그인 X라면 login 페이지로 이동
    },
    clickBtn(btn) {
      this.btn = btn
    }

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
