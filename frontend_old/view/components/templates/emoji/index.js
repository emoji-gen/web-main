import './index.css'
import meta from 'eg/lib/meta'

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
    'eg-generator': require('eg/components/organisms/generator'),
    'eg-recently': require('eg/components/organisms/recently'),
    'eg-result': require('eg/components/organisms/result'),
  },
}
