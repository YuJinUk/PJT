<template>
  <div class="movie-list">
    <br><br>
    <h3 class="text-light">Today Movie</h3>
    <br><br>
    <div class="row row-cols-1 row-cols-md-5 g-4">
    <MovieTodayListItem 
    v-for="movie in Todaymovies" :key="movie.id" :movie="movie"
    />
    </div>
  </div>
</template>

<script>
import MovieTodayListItem from '@/components/MovieTodayListItem'

export default {
  name: 'MovieTodayList',
  components: {
    MovieTodayListItem,
  },
  computed: {
    Todaymovies() {
      return this.$store.state.today_movies
    }
  }
}
</script>

<style>

</style>
