'use strict'

import queryString from 'query-string'
import pick from 'lodash.pick'

import 'flickity/css/flickity.css'
import Flickity from 'flickity'

import './index.css'

module.exports = {
  name: 'eg-recently',
  template: require('./index.html'),

  data() {
    return {
      flkty: null,
      histories: [],
    }
  },

  watch: {
    histories(val, oldVal) {
      if (!this.flkty) { return }

      // clear
      this.flkty.remove(this.flkty.cells)

      // add
      const template = this._makeTemplate()
      for (const history of val) {
        const elem = template.cloneNode(true)
        const url  = this._makeEmojiUrl(history)
        elem.style.backgroundImage = `url('${url}')`
        this.flkty.append(elem)
      }
    },
  },

  ready() {
    this.flkty = new Flickity(this.$els.carousel, {
      contain: true,
      setGallerySize: false,
      wrapAround: true,
    })

    this.$http.get('/api/histories')
      .then(res => {
        this.histories = res.data
      })
  },

  methods: {
    _makeTemplate() {
      const wrapper = document.createElement('div')
      wrapper.innerHTML = require('./cell.html')
      return wrapper.querySelector('*')
    },

    _makeEmojiUrl(history) {
      const query = pick(history, [
        'text',
        'color',
        'back_color',
        'font',
        'size_fixed',
        'align',
        'stretch',
      ])
      return `/emoji?${queryString.stringify(query)}`
    },
  },
}
