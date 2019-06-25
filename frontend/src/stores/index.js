'use strict'

import Vuex from 'vuex'

import app from './app'
import contact from './contact'
import home from './home'

export default () => {
  return new Vuex.Store({
    modules: {
      contact,
      home,
      app,
    },
  })
}
