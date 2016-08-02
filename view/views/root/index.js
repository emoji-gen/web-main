import Vue from 'vue'

import './index.css'

module.exports = {
  name: 'eg-root',
  template: require('./index.html'),
  components: {
    'eg-header': require('../../parts/header'),
    'eg-footer': require('../../parts/footer'),
  },
}
