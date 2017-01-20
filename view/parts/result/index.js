import queryString from 'query-string'
import VueSharer from 'vue-sharer'
import bitly from '../../lib/bitly'

import './index.css'

module.exports = {
  name: 'eg-result',
  template: require('./index.html'),
  data: () => ({
    visibleResult: false,
    visibleShare: false,
    rawText: null,
    rawColor: null,
    rawFont: null,
    queryString: null,
    fonts: [],
    shortenUrl: null,
    chromeExtensionAttached: false,
  }),

  computed: {
    text: function () {
      if (this.rawText) {
        return this.rawText.replace(/\n/, ' ')
      }
      return ''
    },

    color: function () {
      if (this.rawColor) {
        return `#${this.rawColor}`
      }
      return ''
    },
    cssColor: function () {
      if (this.rawColor) {
        return `#${this.rawColor.slice(0, 6)}`
      }
      return ''
    },

    font: function () {
      return this.fonts.find(font => font.key === this.rawFont)
    },
    fontName: function () {
      if (this.font) {
        return this.font.name
      }
      return ''
    },

    emojiUrl: function () {
      if (this.queryString) {
        return `/emoji?${this.queryString}`
      }
      return null
    },
    emojiDownloadUrl: function () {
      if (this.queryString) {
        return `/emoji_download?${this.queryString}`
      }
      return null
    },

    currentUrl: function () {
      return location.href
    },

    progress: function () {
      return !this.shortenUrl
    },
  },

  attached: function () {
    this.$http.get('/api/fonts')
      .then(res => {
        this.fonts = res.data
      })
  },

  events: {
    EG_EMOJI_GENERATE(query) {
      this.rawText  = query.text
      this.rawColor = query.color
      this.rawFont  = query.font

      this.queryString   = queryString.stringify(query)
      this.visibleResult = true
      this.visibleShare  = false
      this.shortenUrl    = null
    },
    CE_ATTACH() {
      this.chromeExtensionAttached = true

      // this.$dispatch('CE_REGISTER_EMOJI', {
      //   url: 'http://localhost:5000/emoji?align=center&back_color=FFFFFF00&color=EC71A1FF&font=notosans-mono-bold&public_fg=true&size_fixed=false&stretch=true&text=%E7%B5%B5%E6%96%87%0A%E5%AD%97%E3%80%82',
      //   text: 'emoji',
      //   teamdomain: 'prismrhythm',
      // })
    },
    CE_SEARCH_JOINED_TEAM_DONE(detail) {
    },
  },

  methods: {
    toggleShare: function () {
      this.visibleShare = !this.visibleShare;

      if (this.visibleShare) {
        this.onShareShown()
      }
    },

    onShareShown: function () {
      if (!this.shortenUrl) {
        bitly.shorten(this.currentUrl)
          .then(url => {
            this.shortenUrl = url
          })
      }
    },
  },

  directives: {
    'eg-sharer': VueSharer,
  },
}
