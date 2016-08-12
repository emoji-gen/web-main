import './index.css'

module.exports = {
  name: 'eg-hatena',
  template: require('./index.html'),
  attached: function () {
    const elem = document.createElement('script')
    elem.type  = 'text/javascript'
    elem.src   = 'https://b.st-hatena.com/js/bookmark_button.js'
    elem.async = true
    this.$el.appendChild(elem)
  },
}
