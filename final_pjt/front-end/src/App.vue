<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">

        <a class="navbar-brand" href="/"><img height="32" src = "@/assets/logo.png" /></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarmenu" aria-controls="navbarmenu" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarmenu">

        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>

          <li v-if="isLogin" class="nav-item">
            <router-link class="nav-link" to="/profile">profile</router-link>
          </li>

          <li v-if="isLogin" class="nav-item">
            <router-link class="nav-link" to="/main">main page</router-link>
          </li>
          
          <li v-if="isLogin" class="nav-item">
            <router-link class="nav-link" to="/predict">predict revenue</router-link>
          </li>
          
        </ul>
          <div v-if="isLogin" class="nav-item">
          <input class="form-control" type="search" placeholder="Search" aria-label="Search" v-model="searchkey" @keyup.enter="search()">
          </div>
          <div v-if="isLogin" class="nav-item d-none d-lg-block">
            <button class="btn btn-outline-light" v-if="isLogin" @click="logout" type="button">logout</button>
          </div>

        </div>
      </div>
    
      
      
      
    </nav>
    <router-view />

  </div>
</template>

<script>
export default {
  data() {
    return {
      searchkey: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    },
  },
  mounted() {
    // this.startCursor()
  },
  methods: {
    logout () {
      this.$store.dispatch('logout')
    },
    search() {
      const searchkey = this.searchkey
      const payload = {
        searchkey
      }
      this.$store.dispatch('search', payload)
      this.searchkey = null
    },
    startCursor() {
      this.$refs.cursor.focus()
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

/* nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
} */
</style>
