import Vue from 'vue'
import VuePtero from 'vue-ptero'
// import VueResource from 'vue-resource'
import VueRouter from 'vue-router'

import App from 'desktop/components/pages/app.vue'

// -----------------------------------------------------------------------------

Vue.use(VuePtero, { target: document.body })
Vue.use(VueRouter)

// -----------------------------------------------------------------------------

const routes = [
  {
    path: '/',
    component: require('desktop/components/templates/emoji.vue'),
  },
]
const router = new VueRouter({
  mode: 'history',
  routes,
})

new Vue({
  router,
  el: '.eg-app',
  render: h => h(App),
})
