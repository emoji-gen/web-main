'use strict'

import Vue from 'vue'
import Vuex from 'vuex'
import VuePtero from 'vue-ptero'
import VueRouter from 'vue-router'

import App from 'desktop/components/pages/app'

// -----------------------------------------------------------------------------

Vue.use(Vuex)
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
const store = new Vuex.Store({
  state: {
    extension: {
      attached: false,
    },
  },
  mutations: {
    attachExtension(state) {
      state.extension.attached = true
    },
  },
  actions: {
    attachExtension(context) {
      context.commit('attachExtension')
    },
  },
})

new Vue({
  el: '.eg-app',
  render: h => h(App),
  router,
  store,
})
