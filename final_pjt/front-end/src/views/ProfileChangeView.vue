<template>
  <div class="background">
    <div class="position-absolute top-50 start-50 translate-middle">
      <h1 class="text-light">New password</h1><br><br>
      <div class="form-floating align-conten-center">
            <input v-model="new_password1"  ref="cursor" type="password" class="form-control" id="floatingPass" placeholder="Password">
            <label for="floatingPass">Password</label>
          
          <div class="form-floating">
            <input v-model="new_password2"  ref="cursor_password" type="password" class="form-control" id="floatingPassword" placeholder="Confirm Password">
            <label for="floatingPassword">Confirm Password</label>
          </div>
          <button @click="profileChange()" class="w-100 btn btn-lg btn-dark">Confirm Password</button>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileChangeView',

  data() {
    return {
      new_password1: null,
      new_password2: null,
    }
  },
  methods: {

    profileChange() {
      // console.log('signup')
      const new_password1 = this.new_password1
      const new_password2 = this.new_password2
      const payload = {
        new_password1, new_password2
      }
      console.log(payload)
      // this.$store.dispatch('profileChange', payload)
      this.$router.push('/')
      alert('홈으로 갑니다.')
    }
  }
}
</script>

<style>
.background {
  height: 100vh;
  width: 100vw;
  background-color: #141414
}
</style>