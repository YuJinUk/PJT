
<template>
  <div class="background">
  <div class="position-absolute top-50 start-50 translate-middle">
    <img src = "@/assets/logo.png" class="img-fluid" />
    <div class="text-light" >
      <h1 v-if="isLogin"> {{this.$store.state.username}} 님이 로그인중입니다. </h1>
      <br>
      <!-- <input type="text" v-model="searchkey" @keyup.enter="search()" value="search">
      <button @click="search()">search</button> -->
    </div>
    <div class="" v-if="!this.isLogin">

      <main class="form-signin w-100 mx-auto">

          <h1 class="h3 mb-3 fw-normal"></h1>

          <div class="form-floating">
            <input v-model="username"  ref="cursor" type="id" class="form-control" id="floatingInput" placeholder="id">
            <label for="floatingInput">ID</label>
          
          <div class="form-floating">
            <input v-model="password"  ref="cursor_password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
            <label for="floatingPassword">Password</label>
          </div>
          <button @click="login()" class="w-100 btn btn-lg btn-dark">Sign in</button>
          </div>
          <!-- //text-muted -->
          <p class="mt-5 mb-3  text-light ">회원이 아니신가요?
            <router-link to="/signup">
              지금 가입하세요
            </router-link>
          </p>
          

      </main>
      </div>
      <!-- <label for="username">사용자명 : </label>
      <input @keyup.enter="Cursor_password" ref="cursor" type="text" id="username" v-model="username"><br>

      <label for="password"> 비밀번호 : </label>
      <input @keyup.enter="login()" ref="cursor_password" type="password" id="password" v-model="password"><br>

      <input @click="login" type="submit" value="확인">
       -->
    <!-- </div> -->
  </div>
  </div>
</template>

<script>

// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {


  },
  data() {
    return {
      username: this.$store.state.username,
      password: null,
      searchkey: null,
    }
  },
  // mounted() {
  //   if(!this.login){this.startCursor()}
  // },
  
  computed: {
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  mounted(){
    this.getUser()
  },
  methods: {
    logout () {
      this.$store.dispatch('/logout')
    },
    login() {
      const username = this.username
      const password = this.password
      // console.log(username)

      if (!username) {
        alert('ID 입력해주세요')
        return
      } else if (!password){
        alert('비밀번호 입력해주세요')
        return
      }

      const payload = {
        username, password
      }

      console.log(payload)

      this.$store.dispatch('login', payload)
    },
    // search() {
    //   const searchkey = this.searchkey
    //   const payload = {
    //     searchkey
    //   }
    //   this.$store.dispatch('search', payload)
    // },

    // startCursor() {
    //   this.$refs.cursor.focus()
    // },
    Cursor_password() {
      this.$refs.cursor_password.focus()
    },
    getUser() {
      this.$store.dispatch('getUser')
      
    },
  }
}
</script>

<style>
.background {
  height: 100vh;
  width: 100vw;
  background-color: #141414
}

.otherColor {
  background-color: #d4d4d4
}
</style>