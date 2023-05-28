<template>
  <div>
    <h5><img :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2/${movie.poster_path}`" alt="" srcset="">{{ movie.poster_path }}</h5>
    <p>{{ movie.title }}</p>
    <p>{{ movie.release_date }}</p>
    <router-link :to="{
      name: 'DetailView',
      params: {id: movie.movie_id }}">
      [DETAIL]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>
