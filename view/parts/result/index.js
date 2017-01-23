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
    EG_EMOJI_GENERATE: function (query) {
      this.rawText  = query.text
      this.rawColor = query.color
      this.rawFont  = query.font

      this.queryString   = queryString.stringify(query)
      this.visibleResult = true
      this.visibleShare  = false
      this.shortenUrl    = null
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
