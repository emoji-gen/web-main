import './index.css'
import meta from 'eg/lib/meta'

module.exports = {
  name: 'eg-root',
  template: require('./index.html'),
  events: {
    EG_EMOJI_GENERATE: function (args) {
      this.$broadcast('EG_EMOJI_GENERATE', args)
    },
    CE_SEARCH_JOINED_TEAMS() {
      this.$ptero.emit('CE_SEARCH_JOINED_TEAMS')
    },
    CE_REGISTER_EMOJI(args) {
      this.$ptero.emit('CE_REGISTER_EMOJI', { detail: args })
    },
  },
  created() {
    this.$ptero.on('CE_ATTACH', e => {
      if (meta.env.debug) {
        console.log('attached by Chrome Extension', e.detail)
      }
      this.$broadcast('CE_ATTACH', e.detail)
    })
    this.$ptero.on('CE_SEARCH_JOINED_TEAMS_DONE', e => {
      if (meta.env.debug) { console.log('CE_SEARCH_JOINED_TEAMS_DONE', e.detail) }
      this.$broadcast('CE_SEARCH_JOINED_TEAMS_DONE', e.detail)
    })
    this.$ptero.on('CE_REGISTER_EMOJI_DONE', e => {
      if (meta.env.debug) { console.log('CE_REGISTER_EMOJI_DONE', e.detail) }
      this.$broadcast('CE_REGISTER_EMOJI_DONE', e.detail)
    })
  },
  components: {
    egBackground: require('eg/components/organisms/background'),
    egFooter: require('eg/components/organisms/footer'),
    egHeader: require('eg/components/organisms/header'),
  }
}
