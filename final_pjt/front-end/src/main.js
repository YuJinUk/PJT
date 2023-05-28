import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import VueCarousel from 'vue-carousel'

Vue.config.productionTip = false
Vue.use(VueCarousel)

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
