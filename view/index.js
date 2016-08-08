import Vue from 'vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'

import './index.css'
import env from './lib/env'

Vue.use(VueResource)
Vue.use(VueRouter)
Vue.http.options.crossOrigin = true

const RootView = Vue.extend(require('./views/root'))
const router   = new VueRouter({
	hashbang: true,
})

router.map(require('./configs/routes'))
router.start(RootView, '.eg-root')

console.log(env)
