import './index.css'

module.exports = {
  name: 'eg-footer',
  template: require('./index.html'),

  directives: {
    'eg-scroll': require('../../directives/scroll'),
  },
}
