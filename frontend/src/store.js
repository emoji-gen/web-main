'use strict'

import Vuex from 'vuex'

// -------------------------------------------------------------------

const extension = {
  namespaced: true,
  state: {
    attached: false,
  },
  mutations: {
    attach(state) {
      state.attached = true
    },
  },
  actions: {
    attach({ commit }) {
      commit('attach')
    },
  },
}

const home = {
  namespaced: true,
  state: {
    fonts: window.HOME_FONTS,
    histories: window.HOME_HISTORIES,
  },
}

// -------------------------------------------------------------------

export default () => {
  return new Vuex.Store({
    modules: {
      extension,
      home,
    },
  })
}
