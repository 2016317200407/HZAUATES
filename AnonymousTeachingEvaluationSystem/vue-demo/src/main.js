import Vue from 'vue'
import App from './App'
import axios from 'axios'
Vue.config.productionTip = false
Vue.prototype.$axios = axios

new Vue({
  router,
  el: '#app',
  components:{ App },
  template:'<App/>'
})
import router from './router'