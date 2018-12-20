'use strict'

export default {
  namespaced: true,
  state: {
    title: document.title,
    extensionAttached: false,
  },
  mutations: {
    setTitle(state, { title }) {
      state.title = title
    },
    attachExtension(state) {
      state.extensionAttached = true
    },
  },
  actions: {
    extensionAttached({ commit }) {
      commit('attachExtension')
    },
  },
}
