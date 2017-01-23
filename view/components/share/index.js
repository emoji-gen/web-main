import VueSharer from 'vue-sharer'
import bitly from '../../lib/bitly'

import './index.css'

module.exports = {
  name: 'eg-share',
  template: require('./index.html'),
  props: {
    visible: Boolean,
  },
  data: () => ({
    shortenUrl: null,
    chromeExtensionAttached: false,
  }),

  computed: {
    currentUrl: function () {
      return location.href
    },

    progress: function () {
      return !this.shortenUrl
    },
  },

  watch: {
    visible(val, oldVal) {
      if (val) {
        this.onShown()
      }
    },
  },

  events: {
    EG_EMOJI_GENERATE(query) {
      this.shortenUrl = null
    },
  },

  methods: {
    onShown: function () {
      if (!this.shortenUrl) {
        bitly.shorten(this.currentUrl)
          .then(url => {
            this.shortenUrl = url
          })
      }
    },
  },

  directives: {
    sharer: VueSharer,
  },
}
