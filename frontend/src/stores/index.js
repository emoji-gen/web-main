'use strict'

import Vuex from 'vuex'

import app from './app'
import contact from './contact'

// -------------------------------------------------------------------


const home = {
  namespaced: true,
  state: {
    fonts: window.HOME_FONTS,
    histories: window.HOME_HISTORIES,
    title: HOME_TITLE,
  },
  actions: {
    mounted({ commit, state: { title } }) {
      commit('app/setTitle', { title }, { root: true })
    },
  },
}


// -------------------------------------------------------------------

export default () => {
  return new Vuex.Store({
    modules: {
      contact,
      home,
      app,
    },
  })
}
