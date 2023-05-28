<template>
  <div style="margin: auto; width: 80%; background-color:white; color: black; padding:20px; border-radius:20px;">
    <h3 style="margin-top: 20px; margin-bottom: 0px;">영화에 대하여 할 말이 있다면?</h3>
      <!-- {{ user }}<br>
      {{ username }}<br>
      {{ email }}<br> -->
      <br>
      <label for="comment"></label>
      <p>댓글을 입력해주세요</p>
      <input @keyup.enter="commentCreate()" ref="cursor_comment" type="text" id="comment" v-model="comment_create">
      &nbsp;
      <input @click="commentCreate()" type="submit" value="확인">
      
    <div class="">
        <div v-for="comment in comments"
        :key="comment.id" :comment="comment"
        >
        <br>
        <div>
            <div class="btn-group" role="group" aria-label="Basic outlined example">
                <button type="button" class="text-dark btn btn-outline-primary">{{ comment.content }}</button>
                <button type="button" class="btn btn-outline-primary" v-if="comment.user === user.pk" @click="deleteComment(comment.comment_id)">삭제</button>
            </div>
        </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieComments',
  components: {
  },

  data() {
    return {
      comments: null,
      comment: null,
      comment_create: null,
      user: this.$store.state.user,
      username: this.$store.state.username,
      email: this.$store.state.email,
      // nickname: this.$store.state.nickname
    }
  },
  created() {
    this.getUser()
    this.getComments()
  },
  methods: {
    getComments(){
        const movie_id = this.$route.params.id
            // const movie_id = this.$route.params.id
        console.log()
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${ movie_id }/allcomments/`,
      })
        .then((res) => {
            this.comments = res.data
            // console.log('------------------------------')
            // console.log(res.data)
            // console.log(this.comments.comment_id)
        })
        .catch((err) => {
        console.log(err)
        })
    },
        deleteComment(id){
            const movie_id = this.$route.params.id
            console.log(id)
            console.log(movie_id)
// movies/<int:movie_id>/allcomments/<int:comments_pk>/
            axios({
                method: 'delete',
                url: `${API_URL}/api/v1/movies/${ movie_id }/allcomments/${id}/`,
                        data:{
                            movie_id, id
                        }
      })
        .then((res) => {
            this.comments = res.data
            console.log(res.data)
        })
        .catch((err) => {
        console.log(err)
        })
    },
    commentCreate(){
      const content = this.comment_create
      const id = this.$route.params.id
      const movie_id = id
      console.log('체크중')
      console.log(movie_id)
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${ movie_id }/comments/`,
        data: {
          content, movie_id
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log('체크중')
          console.log(res)
          // this.$router.push(`${API_URL}/api/v1/movies/${ id }/comments/`)
          // location.reload(true)
          this.comment_create = null
          this.getComments()
        })
        .catch((err) => {
        console.log(err)
        })
    },
    startCursor() {
      this.$refs.cursor_comment.focus()
    },
    getUser() {
      this.$store.dispatch('getUser')
    },
  }
}
</script>

<style>

</style>