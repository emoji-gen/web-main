import Vue      from 'vue'
import {Chrome} from 'vue-color'

import './index.css'

const defaultProps = {
  hex: '#000000',
  rgba: {
    r: 255,
    g: 255,
    b: 255,
    a: 1
  },
  a: 1
}

module.exports = {
  name: 'eg-generator',
  template: require('./index.html'),
  data: () => ({
    colors: defaultProps,
    fonts: [
      { key: 'foo', name: 'AAA Font' },
      { key: 'bar', name: 'AAA Font' },
      { key: 'baz', name: 'AAA Font' },
    ],
  }),
  components: {
    'chrome-picker': Chrome,
  },
}
