import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [],
    today_movies:[],
    token: null,
    userdata: null,
    search_movies: [],
    user: null,
    username: null,
    email: null,
    nickname: null,
    // genre: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_TODAY_MOVIES(state, movies) {
      state.today_movies = movies
    },
    // signup & login -> 완료하면 토큰 발급
    SIGNUP_TOKEN(state, token) {
      
      state.token = token
    //   router.push({name : 'HomeView'}) // store/index.js $router 접근 불가 -> import를 해야함
      // location.reload(true)
    },
    SAVE_TOKEN(state, token) {
      state.token = token
    //   router.push({name : 'MainView'}) // store/index.js $router 접근 불가 -> import를 해야함
      // location.reload(true)
    },
    // LOG_OUT(state) {
    //   state.user = null
    //   state.username = null
    //   state.email = null
    //   // state.nickname = null
    // //   state.genre = null
    //   state.token = null
      
      // router.push({name : 'HomeView'}) // store/index.js $router 접근 불가 -> import를 해야함
    //   location.reload(true)
    // },
    LOG_OUT(state) {
        state.user = null
        state.username = null
        state.email = null
        // state.nickname = null
        state.token = null
        
        if(router.currentRoute.name=='HomeView'){
          router.go(router.currentRoute)
        }else{
          router.push({name: 'HomeView'})
        }
        // router.push({name : 'HomeView'}) // store/index.js $router 접근 불가 -> import를 해야함
        // location.reload(true)
      },
    SEARCH(state, movies) {
        state.search_movies = movies
        console.log(router.currentRoute.name)
        // // router.go(router.currentRoute)
        if(router.currentRoute.name=='SearchView'){
          router.go(router.currentRoute)
        }else{
          router.push({name: 'SearchView'})
        }
    },
    // SEARCH(state, movies) {
    //   state.search_movies = movies
    //   // router.go(router.currentRoute)
    //   router.push({name: 'SearchView'})
    //   // location.reload(true)
    //    // 현재 위치 새로고침
    // }
  },

  actions: {

    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((res) => {
        // console.log(res, context)
          context.commit('GET_MOVIES', res.data)
          // console.log(res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    getTodayMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/today/`,
      })
        .then((res) => {
        // console.log(res, context)

          context.commit('GET_TODAY_MOVIES', res.data)
          // console.log(res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      const email = payload.email
    //   const genre = payload.genre
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2, email
        }
      })
        .then((res) => {
        //   console.log(res)
          this.state.username = res.data.username
          context.commit('SIGNUP_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    profileChange(context, payload) {
      const new_password1 = payload.new_password1
      const new_password2 = payload.new_password2
      axios({
        method:'post',
        url: `${API_URL}/accounts/password/change/`,
        data: {
          new_password1, new_password2
        },
        headers: {
          Authorization: `Token ${this.state.token}`
        }
        })
        .then((res) => {
        //   console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    login(context, payload) {
    //   console.log(payload);
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        } 
      })
        .then((res) => {
        // console.log(res.data.key)
        this.state.username = res.data.username
        context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => 
        console.log(err),
        // location.reload(true)
      )
    },
    logout(context){
      context.commit('LOG_OUT')
    },
    search(context, payload) {
      const query = payload.searchkey
      // console.log(query)
      axios({
        method: 'GET',
        url: `https://api.themoviedb.org/3/search/movie?page=1&language=ko-KR&api_key=c988dcefc9872e7d8eb4a1b1592fd0c8&query=${query}`,
        //url 1페이지만 갖고 오도록 해놓음
      })
      .then((res) => {
        // console.log(res.data.results)
        context.commit('SEARCH', res.data.results)
        })
      .catch((err) => console.log(err))
    },
    getUser() {
      const token = this.state.token
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
        Authorization: `Token ${token}`
        }
      })
      .then((res) => {
        // console.log(token)
        this.state.user = res.data
        this.state.username = res.data.username
        this.state.email = res.data.email
        // this.$store.state.nickname = res.data.email
      })
      .catch((err) => {
        console.log(err)
        // router.push({name : 'HomeView'})
      })
    },
  },
  modules: {
  }
})
