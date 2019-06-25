'use strict'

import Vue from 'vue'

import Background from './organisms/Background'
import Footer from './organisms/Footer'
import Generator from './organisms/Generator'
import Header from './organisms/Header'
import App from './pages/App'
import Contact from './templates/Contact'
import Home from './templates/Home'

Vue.component('Background', Background)
Vue.component('Footer', Footer)
Vue.component('Generator', Generator)
Vue.component('Header', Header)
Vue.component('App', App)
Vue.component('Contact', Contact)
Vue.component('Home', Home)

export {
  Background,
  Footer,
  Header,
  App,
  Contact,
  Home,
}
