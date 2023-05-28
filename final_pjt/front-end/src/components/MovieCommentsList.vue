<template>
  <div class="">
    {{ username }}
    <h3>Comments</h3>

    <div v-for="comment in comments"
    :key="comment.id" :comment="comment"
    >{{ comment.content }}
		<p><button @click="deleteComment(comment.id)">X</button></p>
		</div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieCommentsList',
  components: {
  },

  data() {
    return {
      comments: null,
			comment: null,
      user: this.$store.state.user,
      username: this.$store.state.username,
      email: this.$store.state.email,
      // nickname: this.$store.state.nickname
    }
  },

	created(){
		this.getComments(),
    this.getUser()
	},

  methods: {
    getComments(){
			const movie_id = this.$route.params.
      console.log(this.$store.state.user,)
			
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${ movie_id }/allcomments/`,
      })
        .then((res) => {
					this.comments = res.data
					console.log(res.data)
        })
        .catch((err) => {
        console.log(err)
        })
    },
		deleteComment(id){
			const movie_id = this.$route.params.id
			console.log(id)

			axios({
        method: 'delete',
        url: `${API_URL}/api/v1/comments/${ movie_id }`,
				// data:{
				// 	id
				// }
      })
        .then((res) => {
					this.comments = res.data
					console.log(res.data)
        })
        .catch((err) => {
        console.log(err)
        })
    },
    getUser() {
      this.$store.dispatch('getUser')
    },
  }
}
</script>

<style>

</style>