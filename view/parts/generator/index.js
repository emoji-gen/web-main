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
    fonts: [],
    colors: defaultColors,
    text: '絵文\n字。',
    fontKey: null,
  }),
  created: function () {
    this.$http.get('/api/fonts')
      .then(res => {
        this.fonts = res.data

        if (this.fonts.length > 0) {
          this.fontKey = this.fonts[0].key
        }
      })
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
