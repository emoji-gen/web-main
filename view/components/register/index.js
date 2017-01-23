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
    teams: [],
    selectedTeam: null,
    text: '',
    visibleErrors: false,
  }),

  computed: {
    progressTeams() {
      return this.teams.length === 0
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

    CE_SEARCH_JOINED_TEAMS_DONE(detail) {
      if (detail.contents) {
        this.teams = detail.contents
      }
    },

    CE_REGISTER_EMOJI_DONE(detail) {
      this.progress = false
      this.result   = detail
    },
  },

  methods: {
    onShown() {
      if (this.teams.length === 0) {
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
    }
  },

  components: {
    multiselect: VueMultiselect
  },
}
