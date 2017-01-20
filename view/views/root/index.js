import './index.css'
import meta from '../../lib/meta'

module.exports = {
  name: 'eg-root',
  template: require('./index.html'),
  events: {
    EG_EMOJI_GENERATE: function (args) {
      this.$broadcast('EG_EMOJI_GENERATE', args)
    },
    CE_SEARCH_JOINED_TEAMS() {
      const ce = new CustomEvent('CE_SEARCH_JOINED_TEAMS')
      document.body.dispatchEvent(ce)
    },
    CE_REGISTER_EMOJI(args) {
      const ce = new CustomEvent('CE_REGISTER_EMOJI', { detail: args })
      document.body.dispatchEvent(ce)
    },
  },
  created() {
    document.body.addEventListener('CE_ATTACH', e => {
      if (meta.env.debug) {
        console.log('attached by Chrome Extension', e.detail)
      }
      this.$broadcast('CE_ATTACH', e.detail)
    })
    document.body.addEventListener('CE_SEARCH_JOINED_TEAMS_DONE', e => {
      if (meta.env.debug) { console.log(e.detail) }
      this.$broadcast('CE_SEARCH_JOINED_TEAM_DONE', e.detail)
    })
    document.body.addEventListener('CE_REGISTER_EMOJI_DONE', e => {
      if (meta.env.debug) { console.log(e.detail) }
      this.$broadcast('CE_REGISTER_EMOJI_DONE', e.detail)
    })
  },
  components: {
    'eg-background': require('../../parts/background'),
    'eg-footer': require('../../parts/footer'),
    'eg-header': require('../../parts/header'),
  }
}
