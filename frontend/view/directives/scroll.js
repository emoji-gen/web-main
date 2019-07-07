import SweetScroll from 'sweet-scroll'

function toTop() {
  const sweetScroll = new SweetScroll({ easing: 'easeOutQuad' })
  sweetScroll.toTop(0)
}

module.exports = {
  bind: function () {
    this.el.addEventListener('click', toTop, false)
  },

  unbind: function () {
    this.el.removeEventListener('click', toTop, false)
  },
}
