import meta from '../meta'

if (!meta.env.debug) {
  require('./snippet')
} else {
  window.ga = {}
}

module.exports = window.ga
