'use strict'

export default {
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
