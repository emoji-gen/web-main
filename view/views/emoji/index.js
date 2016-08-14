import Vue from 'vue'

import './index.css'

module.exports = {
  name: 'eg-emoji',
  template: require('./index.html'),
  components: {
    'eg-generator': require('../../parts/generator'),
    'eg-recently': require('../../parts/recently'),
    'eg-result': require('../../parts/result'),
  },
  route: {
    activate: function () {
      if (~this.$route.path.indexOf('/emoji')) {
        this.$dispatch('EG_EMOJI_GENERATE', this.$route.query)
      }
    },
  }
}
