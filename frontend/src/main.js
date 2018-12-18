'use strict'

import Vue from 'vue'
import Vuex from 'vuex'
import VuePtero from 'vue-ptero'
import VueRouter from 'vue-router'

import 'normalize.css'

import './style.scss'
import './components'

// -------------------------------------------------------------------

Vue.use(Vuex)
Vue.use(VuePtero, { target: document.body })
Vue.use(VueRouter)

// -------------------------------------------------------------------

