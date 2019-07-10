'use strict'

import VueRouter from 'vue-router'

import { toLocalizedPath, LOCALES } from '@/src/locales'
import { Contact, Home } from './components'


// -------------------------------------------------------------------
// Routes
// -------------------------------------------------------------------

const routes = []
for (const locale of LOCALES) {
  routes.push(
    {
      path: toLocalizedPath('/', locale),
      component: Home,
    },
    {
      path: toLocalizedPath('/result', locale),
      component: Home,
    },
    {
      path: toLocalizedPath('/contact', locale),
      component: Contact,
    }
  )
}


// -------------------------------------------------------------------

export default () => {
  const router = new VueRouter({
    mode: 'history',
    routes,
  })

  router.beforeEach((to, from, next) => {
    // Migrate hash mode to history mode.
    // ref. https://github.com/emoji-gen/web-main/blob/14dc13707e40584becdbd2f73752209891e1215a/frontend/view/configs/routes.js
    if (to.fullPath === '/#!/') {
      next({ path: '/' })
      return
    }
    if (to.fullPath === '/#!/contact') {
      next({ path: '/contact' })
      return
    }
    if (to.fullPath.startsWith('/#!/emoji')) {
      next({ path: to.fullPath.replace(/^\/#!\/emoji/, '/result') })
      return
    }

    next()
  })

  return router
}
