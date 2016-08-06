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
      { key: 'noto-sans-mono-cjk-bold', name: 'Noto Sans Mono CJK Bold' },
      { key: 'mikachan-pb',             name: 'みかちゃん PB' },
      { key: 'migu-1m-bold',            name: 'Migu 1m Bold' },
      { key: 'mplus-1p-black',          name: 'M+ 1p Black' },
      { key: 'aoyagireishoshimo',       name: '青柳隷書しも' },
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
