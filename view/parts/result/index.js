import './index.css'

module.exports = {
  name: 'eg-result',
  template: require('./index.html'),
  data: () => ({
    visibleShare: false,
  }),

  methods: {
    toggleShare: function () {
      this.visibleShare = !this.visibleShare;
    },
  },

  directives: {
    'eg-sharer': require('../../directives/sharer'),
  },
}
