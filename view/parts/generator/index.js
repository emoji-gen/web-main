import Vue       from 'vue'
import {Chrome}  from 'vue-color'
import {sprintf} from 'sprintf-js'

import './index.css'

const defaultColors = {
  hex: '#EC71A1',
  rgba: {
    r: 236,
    g: 113,
    b: 161,
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

  computed: {
    rgbaHex: function () {
      const rgbHex = this.colors.hex.replace(/^#/, '')
      const aHex   = sprintf('%02X', Math.floor(this.colors.rgba.a * 0xff) & 0xff)
      return rgbHex + aHex
    },
  },

  attached: function () {
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
      const query = {
        text: this.text,
        color: this.rgbaHex,
        font: this.fontKey,
      }
      this.$dispatch('EG_EMOJI_GENERATE', query)
      this.$router.go({
        path: '/emoji',
        query,
        replace: true,
      })
    },
  },

  directives: {
    'eg-scroll': require('../../directives/scroll'),
  },
  components: {
    'chrome-picker': Chrome,
  },
}
