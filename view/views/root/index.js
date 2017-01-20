import './index.css'
import meta from '../../lib/meta'

module.exports = {
  name: 'eg-root',
  template: require('./index.html'),
  events: {
    EG_EMOJI_GENERATE: function (args) {
      this.$broadcast('EG_EMOJI_GENERATE', args)
    },
  },
  created() {
    document.body.addEventListener('CE_ATTACH', e => {
      if (meta.env.debug) {
        console.log('attached by Chrome Extension', e.detail)
      }
      this.$broadcast('CE_ATTACH', e.detail)
    })
    document.body.addEventListener('CE_SEARCH_JOINED_TEAMS_END', e => {
      this.$broadcast('CE_SEARCH_JOINED_TEAM_END', e.detail)
    })
  },
  components: {
    'eg-background': require('../../parts/background'),
    'eg-footer': require('../../parts/footer'),
    'eg-header': require('../../parts/header'),
  }
}
