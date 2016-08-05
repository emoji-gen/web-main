import Vue from 'vue'

import './index.css'


module.exports = {
  name: 'eg-home',
  template: require('./index.html'),
  components: {
    'eg-generator': require('../../parts/generator'),
    'eg-recently': require('../../parts/recently'),
  },
}
