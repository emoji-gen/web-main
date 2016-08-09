import SweetScroll from 'sweet-scroll'

const sweetScroll = new SweetScroll({ easing: 'easeOutQuad' })
const toTop       = sweetScroll.toTop.bind(sweetScroll, 0)

module.exports = {
  bind: function () {
    this.el.addEventListener('click', toTop, false)
  },

  unbind: function () {
    this.el.removeEventListener('click', toTop, false)
  },
}
