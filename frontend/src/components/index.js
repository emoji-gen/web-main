'use strict'

import Vue from 'vue'

import ColorKind from './atomics/ColorKind'
import DocumentTitle from './atomics/DocumentTitle'
import HeaderTitle from './molecules/HeaderTitle'
import HeaderLanguage from './molecules/HeaderLanguage'
import Register from './molecules/Register'
import Share from './molecules/Share'
import Background from './organisms/Background'
import Footer from './organisms/Footer'
import Generator from './organisms/Generator'
import Header from './organisms/Header'
import RecentlyLog from './organisms/RecentlyLog'
import Result from './organisms/Result'
import App from './pages/App'
import Contact from './templates/Contact'
import Home from './templates/Home'

Vue.component('ColorKind', ColorKind)
Vue.component('DocumentTitle', DocumentTitle)
Vue.component('HeaderTitle', HeaderTitle)
Vue.component('HeaderLanguage', HeaderLanguage)
Vue.component('Register', Register)
Vue.component('Share', Share)
Vue.component('Background', Background)
Vue.component('Footer', Footer)
Vue.component('Generator', Generator)
Vue.component('Header', Header)
Vue.component('RecentlyLog', RecentlyLog)
Vue.component('Result', Result)
Vue.component('App', App)
Vue.component('Contact', Contact)
Vue.component('Home', Home)

export {
  ColorKind,
  DocumentTitle,
  HeaderTitle,
  HeaderLanguage,
  Register,
  Share,
  Background,
  Footer,
  Generator,
  Header,
  RecentlyLog,
  Result,
  App,
  Contact,
  Home,
}
