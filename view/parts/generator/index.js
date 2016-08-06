import Vue      from 'vue'
import {Chrome} from 'vue-color'

import './index.css'

const defaultColors = {
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
    colors: defaultColors,
    fonts: [
      { key: 'noto', name: 'Noto Sans CJK' },
      { key: 'bar', name: 'AAA Font' },
      { key: 'baz', name: 'AAA Font' },
    ],
    selectedFontKey: null,
  }),
  created: function () {
    this.selectedFontKey = this.fonts[0].key
  },

  components: {
    'chrome-picker': Chrome,
  },
}
