'use strict'

import Vue from 'vue'
import Vuex from 'vuex'
import VuePtero from 'vue-ptero'
import VueRouter from 'vue-router'

import 'normalize.css'

import './style.scss'
import { App } from './components'

// -------------------------------------------------------------------

Vue.use(Vuex)
Vue.use(VuePtero, { target: document.body })
Vue.use(VueRouter)

// -------------------------------------------------------------------

new Vue({
  el: '.App',
  render: h => h(App),
})

