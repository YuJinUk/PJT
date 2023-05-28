import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DetailView from '../views/DetailView.vue'
import ProfileView from '../views/ProfileView.vue'
import ProfileChangeView from '../views/ProfileChangeView.vue'
import MainView from '../views/MainView.vue'
import SearchView from '../views/SearchView.vue'
import SignupView from '../views/SignupView.vue'
import PredictMovieView from '../views/PredictMovieView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/movie/:id',
    name: 'DetailView',
    component: DetailView
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/profileChange',
    name: 'ProfileChangeView',
    component: ProfileChangeView
  },
  {
    path: '/main',
    name: 'MainView',
    component: MainView
  },
  {
    path: '/search',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/predict',
    name: 'PredictMovieView',
    component: PredictMovieView
  },



]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
