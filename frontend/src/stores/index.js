'use strict'

import Vuex from 'vuex'

import app from './app'
import contact from './contact'
import home from './home'
import generator from './generator'

export default () => {
  return new Vuex.Store({
    modules: {
      contact,
      home,
      app,
      generator,
    },
  })
}
