import Vue from 'vue'
import VuePtero from 'vue-ptero'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'

import './index.css'
import 'eg/lib/ga'

Vue.use(VuePtero, { target: document.body })
Vue.use(VueResource)
Vue.use(VueRouter)

const RootView = Vue.extend(require('eg/components/pages/root'))
const router   = new VueRouter({
  hashbang: true,
  saveScrollPosition: false,
})

router.map(require('eg/configs/routes'))
router.start(RootView, '.eg-root')
