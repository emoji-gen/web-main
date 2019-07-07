import './index.css'

module.exports = {
  name: 'eg-color-kind',
  template: require('./index.html'),
  props: {
    'color-kind': String,
    default: 'foreground',
  },
}
