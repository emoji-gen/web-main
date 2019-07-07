import meta from '../meta'

if (!meta.env.debug) {
  require('./snippet')
} else {
  window.ga = function () { };
}

module.exports = window.ga
