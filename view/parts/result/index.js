import queryString from 'query-string'

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
  }),

  events: {
    EG_EMOJI_GENERATE: function (params) {
      this.rawText  = params.text
      this.rawColor = params.color
      this.rawFont  = params.font

      const query = {
        text: params.text,
        color: params.color,
        font: params.font.key,
      }
      this.queryString   = queryString.stringify(query)
      this.visibleResult = true
    },
  },

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
    fontName: function () {
      if (this.rawFont) {
        return this.rawFont.name
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
  },

  methods: {
    toggleShare: function () {
      this.visibleShare = !this.visibleShare;
    },
  },

  directives: {
    'eg-sharer': require('../../directives/sharer'),
  },
}
