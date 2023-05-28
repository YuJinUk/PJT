<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username"> 사용자명 : </label>
      <input type="text" id="username" v-model="username"><br>
        <br>
      <label for="password1"> 비밀번호 : </label>
      <input type="password" id="password1" v-model="password1"><br>
        <br>
      <label for="password2"> 비밀번호 확인 : </label>
      <input type="password" id="password2" v-model="password2">
      <br><br>
      <label for="email"> 이메일 : </label>
      <input type="email" id="email" v-model="email">
        <br><br>
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      email: null,
    //   genre: null,
    }
  },
  methods: {
    signUp() {
      // console.log('signup')
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const email = this.email
    //   const genre = this.genre
      const payload = {
        username, password1, password2, email
      }

      this.$store.dispatch('signUp', payload)
      this.$router.push('/')

    }
  }
}
</script>
