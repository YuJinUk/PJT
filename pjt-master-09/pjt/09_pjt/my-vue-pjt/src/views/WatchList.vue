<template>
  <div>
    <h1>보고싶은 영화</h1>
    <div>
    <input type="text" v-model="want_movie" @keyup.enter="addMovie()">
    <button @click="addMovie()">Add</button>
    </div>
    <br><br>
    <div>
        <ul v-for="(check_list, index) in want_movie_list" :key="index">
            <li>
                <button :class="{'strike-through' : check_list.is_completed}" style="border:None; background-color:white;" @click="deleteMovie(index)">{{check_list.want_movie_value}}</button>
            </li>
        </ul>
    </div>
  </div>
</template>

<script>

export default {
    name : 'WatchList',
    data() {
        return {
            want_movie: null,
            want_movie_list: [],
            movie_idx: null,
            line_list: [],
        }
    },
    methods: {
        addMovie() {
            // console.log(want_movie_value)
            const want_movie_value = this.want_movie
            if (want_movie_value != null) {
                this.want_movie_list.push({want_movie_value, is_completed : false})
                console.log(this.want_movie_list)
                this.want_movie = null
            } else {
                this.want_movie = null
            }

        },
        deleteMovie(idx) {
            const movielist = this.want_movie_list
            // console.log(movielist)
            // console.log(idx)
            const movieindex = idx
            // console.log(movielist[movieindex].is_completed)
            movielist[movieindex].is_completed = !movielist[movieindex].is_completed

            // movielist.splice(movieindex, 1)
            // console.log(movielist)
            // this.want_movie_list = movielist
        }
    },
}
</script>

<style>
.strike-through {
    text-decoration: line-through;
}
</style>