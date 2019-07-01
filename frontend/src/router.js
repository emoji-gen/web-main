'use strict'

import VueRouter from 'vue-router'

import { Contact, Home } from './components'

// -------------------------------------------------------------------

const routes = [
  {
    path: '/',
    component: Home,
  },
  {
    path: '/result',
    component: Home,
  },
  {
    path: '/contact',
    component: Contact,
  },
]

// -------------------------------------------------------------------

export default () => {
  return new VueRouter({
    mode: 'history',
    routes,
  })
}
