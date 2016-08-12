import Vue from 'vue'

import './index.css'

module.exports = {
  name: 'eg-result',
  template: require('./index.html'),
  components: {
    'eg-facebook': require('../../components/facebook'),
    'eg-hatena': require('../../components/hatena'),
  },
}
