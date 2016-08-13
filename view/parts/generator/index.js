import Vue      from 'vue'
import {Chrome} from 'vue-color'

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
    font: function () {
      return this.fonts.find(font => font.key === this.fontKey)
    },
  },

  created: function () {
    this.$http.get('/api/fonts')
      .then(res => {
        this.fonts = res.data

        if (this.fonts.length > 0) {
          this.fontKey = this.fonts[0].key
        }

        this.generate()
      })
  },

  methods: {
    // Run emoji generator
    generate: function () {
      const params = {
        text: this.text,
        color: this.colors.hex.replace(/^#/, ''),
        font: this.font,
      }
      this.$dispatch('EG_EMOJI_GENERATE', params)
    },
  },

  components: {
    'chrome-picker': Chrome,
  },
}
