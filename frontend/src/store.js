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

// -------------------------------------------------------------------

export default () => {
  return new Vuex.Store({
    modules: {
      extension,
    },
  })
}
