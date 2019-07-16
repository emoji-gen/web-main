'use strict'

import Vue from 'vue'
import VueAnalytics from 'vue-analytics'
import VuePtero from 'vue-ptero'
import VueRouter from 'vue-router'
import VueI18n from 'vue-i18n'

import log from 'loglevel'

import 'normalize.css'
import './style.scss'

import { App } from '@/src/components'
import { INITIAL_LOCALE, MESSAGES } from '@/src/locales'
import setupRouter from '@/src/router'


// -------------------------------------------------------------------

const router = setupRouter()

if (DEBUG) {
  log.setLevel('trace')
} else {
  log.setLevel('warn')
}

Vue.use(VueAnalytics, {
  id: 'UA-82501423-1',
  router,
  autoTracking: {
    pageviewOnLoad: false
  },
})

Vue.use(VuePtero, { target: document.body })
Vue.use(VueRouter)
Vue.use(VueI18n)

const i18n = new VueI18n({
  locale: INITIAL_LOCALE,
  messages: MESSAGES,
})

// -------------------------------------------------------------------

export default new Vue({
  el: '.App',
  render: h => h(App),

  /**
   * vue-router
   */
  router,

  /**
   * vue-i18n
   */
  i18n,
})

