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

const defaultBackgroundColors = {
  hex: '#FFFFFF',
  rgba: {
    r: 255,
    g: 255,
    b: 255,
    a: 0
  },
  a: 0
}

module.exports = {
  name: 'eg-generator',
  template: require('./index.html'),
  data: () => ({
    // TODO: サーバーから取得する
    fonts: [],
    colorKind: 'foreground',
    colors: defaultColors,
    backgroundColors: defaultBackgroundColors,
    text: '絵文\n字。',
    fontKey: null,
    publicFg: true,
  }),

  computed: {
    rgbaHex: function () {
      return this.colorsToRgbaHex(this.colors)
    },
    backgroundRgbaHex: function () {
      return this.colorsToRgbaHex(this.backgroundColors)
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
        back_color: this.backgroundRgbaHex,
        font: this.fontKey,
        public_fg: this.publicFg,
      }
      this.$dispatch('EG_EMOJI_GENERATE', query)
      this.$router.go({
        path: '/emoji',
        query,
        replace: true,
      })
    },

    colorsToRgbaHex: function (colors) {
      const rgbHex = colors.hex.replace(/^#/, '')
      const aHex   = sprintf('%02X', Math.floor(colors.a * 0xff) & 0xff)
      return rgbHex + aHex
    },
  },

  directives: {
    'eg-scroll': require('../../directives/scroll'),
  },
  components: {
    'chrome-picker': Chrome,
    'eg-color-kind': require('../../components/color_kind'),
  },
}
