import 'flickity/css/flickity.css'
import Flickity from 'flickity'

import './index.css'

module.exports = {
  name: 'eg-recently',
  template: require('./index.html'),
  ready: function () {
    new Flickity(this.$els.carousel, {
      contain: true,
      setGallerySize: false,
      wrapAround: true,
    })
  },
}
