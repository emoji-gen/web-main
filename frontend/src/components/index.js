'use strict'

import Vue from 'vue'

import Background from './organisms/Background'
import Header from './organisms/Header'
import App from './pages/App'
import Home from './templates/Home'

Vue.component('Background', Background)
Vue.component('Header', Header)
Vue.component('App', App)
Vue.component('Home', Home)

export { App }
