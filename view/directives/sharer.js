import Sharer from 'sharer.npm.js'
import bitly from '../lib/bitly'

function share(e) {
  const sharer = new Sharer(e.target)
  sharer.share()
}

module.exports = {
  bind: function () {
    this.el.addEventListener('click', share, false)
  },

  unbind: function () {
    this.el.removeEventListener('click', share, false)
  },
}
