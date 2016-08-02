import Vue from 'vue'
import VueResource from 'vue-resource'

import './index.css'
import RootView from './views/root'

Vue.use(VueResource)
Vue.http.options.crossOrigin = true

new Vue({
  el: 'body',
  components: {
    // entry point
    'eg-root': RootView,
  },
})
