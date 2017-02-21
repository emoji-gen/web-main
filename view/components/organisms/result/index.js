import browser from 'detect-browser'
import queryString from 'query-string'

import './index.css'

module.exports = {
  name: 'eg-result',
  template: require('./index.html'),
  data: () => ({
    visibleResult: false,
    visibleShare: false,
    visibleRegister: false,
    rawText: null,
    rawColor: null,
    rawFont: null,
    queryString: null,
    fonts: [],
    hasBrowserExtension: false,
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

    isRegisterSupportedBrowser() {
      return browser.name === 'chrome'
    },
    visibleRegisterButton() {
      return this.hasBrowserExtension || this.isRegisterSupportedBrowser
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

      this.queryString     = queryString.stringify(query)
      this.visibleResult   = true
      this.visibleRegister = false
      this.visibleShare    = false

      return true
    },
    CE_ATTACH() {
      this.hasBrowserExtension = true
      return true
    },
  },

  methods: {
    toggleShare() {
      if (this.visibleShare) {
        this.visibleShare    = false
      } else {
        this.visibleShare    = true
        this.visibleRegister = false
      }
    },

    toggleRegister() {
      if (this.visibleRegister) {
        this.visibleRegister = false
      } else {
        this.visibleRegister = true
        this.visibleShare    = false
      }
    },
  },

  components: {
    'eg-share': require('eg/components/molecules/share'),
    'eg-register': require('eg/components/molecules/register'),
  },
}
