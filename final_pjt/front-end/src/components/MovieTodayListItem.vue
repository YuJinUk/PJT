<template>
  <div>
  <div class="col">
    <div class="card h-100">
        <!-- {{ movie.poster_path }} -->
        <router-link :to="{
            name: 'DetailView',
            params: {id: movie.movie_id }}">
            <img class="card-img-top" :src="`https://image.tmdb.org/t/p/w600_and_h900_bestv2/${movie.poster_path}`">
        </router-link>
      <!-- <div class="card-body">
        <h5 class="card-title"> {{ movie.title }} </h5>
        <p class="card-text"> {{ movie.overview }} </p>
        
      </div> -->
    </div>
  </div>
    <!-- <p>{{ movie.title }}</p>
    <p>{{ movie.release_date }}</p> -->
    <!-- <router-link :to="{
      name: 'DetailView',
      params: {id: movie.movie_id }}">
      [DETAIL]
    </router-link> -->
    <!-- <hr> -->
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
  width: 200px;
  height: 250px;
  margin-top: 50px;
}
</style>