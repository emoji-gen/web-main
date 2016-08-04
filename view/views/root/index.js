import Vue from 'vue'

import './index.css'

module.exports = {
  name: 'eg-root',
  template: require('./index.html'),
  components: {
    'eg-background': require('../../parts/background'),
    'eg-footer': require('../../parts/footer'),
    'eg-header': require('../../parts/header'),
  },
}
