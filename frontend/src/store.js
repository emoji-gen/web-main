'use strict'

import Vuex from 'vuex'

// -------------------------------------------------------------------

const app = {
  namespaced: true,
  state: {
    title: document.title,
  },
  mutations: {
    setTitle(state, { title }) {
      state.title = title
    },
  },
}

const contact = {
  namespaced: true,
  state: {
    title: window.CONTACT_TITLE,
  },
  actions: {
    mounted({ commit, state: { title } }) {
      commit('app/setTitle', { title }, { root: true })
    },
  },
}


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
    title: window.HOME_TITLE,
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
      extension,
      home,
      app,
    },
  })
}
