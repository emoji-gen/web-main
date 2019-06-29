'use strict'

import Vue from 'vue'

import ColorKind from './atomics/ColorKind'
import Background from './organisms/Background'
import Footer from './organisms/Footer'
import Generator from './organisms/Generator'
import Header from './organisms/Header'
import RecentlyLog from './organisms/RecentlyLog'
import App from './pages/App'
import Contact from './templates/Contact'
import Home from './templates/Home'

Vue.component('ColorKind', ColorKind)
Vue.component('Background', Background)
Vue.component('Footer', Footer)
Vue.component('Generator', Generator)
Vue.component('Header', Header)
Vue.component('RecentlyLog', RecentlyLog)
Vue.component('App', App)
Vue.component('Contact', Contact)
Vue.component('Home', Home)

export {
  ColorKind,
  Background,
  Footer,
  Generator,
  Header,
  RecentlyLog,
  App,
  Contact,
  Home,
}
