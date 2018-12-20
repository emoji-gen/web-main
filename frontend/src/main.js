'use strict'

import Vue from 'vue'
import Vuex from 'vuex'
import VuePtero from 'vue-ptero'
import VueRouter from 'vue-router'
import VueSharer from 'vue-sharer'

import log from 'loglevel'

import 'normalize.css'
import './style.scss'

import { App } from './components'
import setupRouter from './router'
import setupStore from './store'

// -------------------------------------------------------------------

if (DEBUG) {
  log.setLevel('trace')
} else {
  log.setLevel('warn')
}

Vue.use(Vuex)
Vue.use(VuePtero, { target: document.body })
Vue.use(VueRouter)

Vue.directive('sharer', VueSharer)

// -------------------------------------------------------------------

export default new Vue({
  el: '.App',
  render: h => h(App),
  router: setupRouter(),
  store: setupStore(),
})

