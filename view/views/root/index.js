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
    const _this = this
    document.body.addEventListener('chrome_extension:attach', function (e) {
      if (meta.env.debug) {
        console.log('Chrome Extension attached', e.detail)
      }
      _this.$broadcast('EG_CHROME_EXTENSION_ATTACHED', e.detail)
    })
  },
  components: {
    'eg-background': require('../../parts/background'),
    'eg-footer': require('../../parts/footer'),
    'eg-header': require('../../parts/header'),
  },
}
