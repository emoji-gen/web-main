'use strict'

export default {
  namespaced: true,
  state: {
    title: CONTACT_TITLE,
  },
  actions: {
    mounted({ commit, state: { title } }) {
      commit('app/setTitle', { title }, { root: true })
    },
  },
}

