import './index.css'

module.exports = {
  name: 'eg-header',
  template: require('./index.html'),
  directives: {
    'eg-sharer': require('../../directives/sharer'),
  },
}
