import url from 'url'
import VueMultiselect from 'vue-multiselect'

import './index.css'

module.exports = {
  name: 'eg-register',
  template: require('./index.html'),
  props: {
    visible: Boolean,
    emojiUrl: String,
  },

  data: () => ({
    progress: false,
    result: {},
    selected: null,
    teams: null,
    selectedTeam: null,
    text: '',
    visibleErrors: false,
    hasBrowserExtension: false,
  }),

  computed: {
    teamsOrEmptyArray() {
      if (Array.isArray(this.teams)) {
        return this.teams
      }
      return []
    },

    progressTeams() {
      return !Array.isArray(this.teams)
    },

    hasErrorMessages() {
      return this.errorMessages.length > 0
    },

    errorMessages() {
      const messages = []

      if (!this.selectedTeam) {
        messages.push('チームが選択されていません。')
      }
      if (this.text.length === 0) {
        messages.push('絵文字の名前が入力されていません。')
      }

      return messages
    },
  },

  watch: {
    visible(val, oldVal) {
      if (val) {
        this.onShown()
      }
    },
  },

  events: {
    EG_EMOJI_GENERATE() {
      this.result        = {}
      this.text          = ''
      this.visibleErrors = false
    },

    CE_ATTACH() {
      this.hasBrowserExtension = true
    },
    CE_SEARCH_JOINED_TEAMS_DONE(detail) {
      if (detail.contents) {
        const teams = [].concat(detail.contents)
        teams.sort((a, b) =>
          a.name < b.name ? -1 :
          a.name > b.name ?  1 : 0) // alphabetical order
        this.teams = teams
      }
    },

    CE_REGISTER_EMOJI_DONE(detail) {
      this.progress = false

      if (detail.err && typeof detail.err !== 'string') {
        this.result = { err: '不明なエラーが発生しました' }
      } else {
        this.result = detail
      }
    },
  },

  methods: {
    onShown() {
      const isEmpty = this.teamsOrEmptyArray.length === 0
      if (this.hasBrowserExtension && isEmpty) {
        this.$dispatch('CE_SEARCH_JOINED_TEAMS')
      }
    },

    updateSelectedTeam(newSelected) {
      this.selectedTeam = newSelected
    },

    register() {
      this.visibleErrors = true
      if (this.hasErrorMessages > 0) {
        return
      }

      const args = {
        teamdomain: this.selectedTeam.teamdomain,
        url: url.resolve(location.href, this.emojiUrl),
        text: this.text,
      }
      this.progress = true
      this.result   = {}
      this.$dispatch('CE_REGISTER_EMOJI', args)
    },

    registerByKeyPress(e) {
      if (e.keyCode === 13) { // Enter
        if (this.selectedTeam && this.text.length > 0) {
          this.register()
        }
      }
    },
  },

  components: {
    multiselect: VueMultiselect
  },
}
