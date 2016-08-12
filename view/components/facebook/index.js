import queryString from 'query-string'

import './index.css'

const baseUrl = 'https://www.facebook.com/plugins/share_button.php'
const defaultParameters = {
  layout: 'box_count',
  size: 'large',
  mobile_iframe: 'true',
  appId: '1668136526839121',
  width: '75',
  height: '58'
}

module.exports = {
  name: 'eg-facebook',
  template: require('./index.html'),

  props: ['url'],
  computed: {
    iframeUrl: function () {
      const params = Object.assign({ href: this.url }, defaultParameters)
      const paramsString = queryString.stringify(params)
      return `${baseUrl}?${paramsString}`
    },
  },
}
