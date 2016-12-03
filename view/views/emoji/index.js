import './index.css'
import meta from '../../lib/meta'

module.exports = {
  name: 'eg-emoji',
  template: require('./index.html'),

  data() {
    return {
      historyEnabled: meta.feature.history,
    }
  },

  route: {
    activate: function () {
      if (~this.$route.path.indexOf('/emoji')) {
        this.$dispatch('EG_EMOJI_GENERATE', this.$route.query)
      }
    },
  },
  components: {
    'eg-generator': require('../../parts/generator'),
    'eg-recently': require('../../parts/recently'),
    'eg-result': require('../../parts/result'),
  },
}
