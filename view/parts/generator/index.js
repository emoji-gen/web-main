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
    // TODO: サーバーから取得する
    fonts: [
      { key: 'noto-sans-mono-cjk-bold', name: 'Noto Sans Mono CJK Bold' },
      { key: 'mikachan-pb',             name: 'みかちゃん PB' },
      { key: 'migu-1m-bold',            name: 'Migu 1m Bold' },
      { key: 'mplus-1p-black',          name: 'M+ 1p Black' },
      { key: 'aoyagireishoshimo',       name: '青柳隷書しも' },
    ],
    colors: defaultColors,
    text: '絵文\n字。',
    fontKey: null,
  }),
  created: function () {
    this.fontKey = this.fonts[0].key
  },

  methods: {
    // Run emoji generator
    generate: function () {
      console.log('generate')
    },
  },

  components: {
    'chrome-picker': Chrome,
  },
}
