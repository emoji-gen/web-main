'use strict'

import VueRouter from 'vue-router'

import { Home } from './components'

// -------------------------------------------------------------------

const routes = [
  {
    path: '/',
    component: Home,
  },
]

// -------------------------------------------------------------------

export default function() {
  return new VueRouter({
    mode: 'history',
    routes,
  })
}
