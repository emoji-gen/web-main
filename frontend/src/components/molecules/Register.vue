<template>
  <div class="Register" :class="{'progress': progress}">
    <div class="overlay"></div>
    <div class="inner" v-if="browserExtensionEnabled">
      <div class="inputs">
        <div class="group teams">
          <label v-t="'Register.inputs_team_label'"></label>
          <multiselect
            label="name"
            :options="teamsOrEmptyArray"
            :close-on-select="true"
            :show-labels="false"
            :loading="progressTeams"
            :placeholder="$t('Register.inputs_team_placeholder')"
            v-model="selected"
            @input="updateSelectedTeam"
          >
            <template slot="noOptions">
              {{ $t('Register.inputs_team_no_options') }}
            </template>
          </multiselect>
        </div>
        <div class="group name">
          <label v-t="'Register.inputs_name_label'"></label>
          <input type="text" :placeholder="$t('Register.inputs_name_placeholder')"
            v-model="text" @keypress="registerByKeyPress">
        </div>
      </div>

      <div class="messages error" v-if="visibleErrors && hasErrorMessages">
        <label v-t="'Register.messages_validation_error_label'"></label>
        <p v-for="errorMessage in errorMessages">{{ errorMessage }}</p>
      </div>

      <div class="messages" v-if="result.contents">
        <label v-t="'Register.messages_successful_label'"></label>
        <p>{{ result.contents }}</p>
      </div>

      <div class="messages error" v-if="result.err">
        <label v-t="'Register.messages_failure_label'"></label>
        <p>{{ result.err }}</p>
      </div>

      <div class="buttons">
        <button type="button" @click="register" v-t="'Register.register_button'"></button>
      </div>

      <div class="help">
        <p v-t="'Register.help_about_teams'"></p>
        <p>{{ $t('Register.help_login_head') }}
          <a href="https://slack.com/signin" target="_blank" rel="nofollow noopener" v-t="'Register.help_login_link_label'"></a>
          {{ $t('Register.help_login_tail') }}</p>
      </div>
    </div>

    <!-- Install -->
    <div class="inner" v-else>
      <h3 v-t="'Register.install_label'"></h3>
      <div class="description">
        <p v-html="$t('Register.install_description')"></p>
      </div>

      <div class="download">
        <ChromeBanner v-if="browser.name === 'chrome'"/>
        <a href="https://addons.mozilla.org/ja/firefox/addon/emoji-generator/"
          target="_blank" rel="noopener"
          v-if="browser.name == 'firefox'">
          <img src="/assets/img/firefox_add_on.png" width="172" height="60" alt="GET THE ADD-ON">
        </a>
      </div>
    </div>
  </div>
</template>


<style lang="scss">
  @import 'includes/_variables';

  %_block-label {
    display: block;
    margin: 0 0 8px 0;
    text-align: center;
    font-size: $font-medium;
    font-weight: bold;
    color: $color-blue-dark;
  }
  %_help_text {
    color: $color-gray;
    font-size: $font-small;
    letter-spacing: .5px;
  }

  .Register {
    position: relative;
    padding: 20px 0 20px;
    line-height: 1.55;

    .inner {
      display: flex;
      flex: 1 1 auto;
      flex-direction: column;
      align-content: flex-start;
      align-items: center;
      margin: 0 auto;
      padding: 10px 0 10px 0;
      transition: opacity .8s ease-in-out;
      opacity: 1;
    }


    /**
     * Loading
     */
    &.progress {
      .overlay {
        display: block;
        z-index: 100;
      }
    }
    .overlay {
      display: none;
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      background-image: url($site-url + '/assets/img/loading_red.gif');
      background-position: center center;
      background-size: 40px auto;
      background-repeat: no-repeat;
      background-color: rgba(255, 255, 255, .6);
    }

    /**
     * Inputs
     */
    .inputs {
      label {
        @extend %_block-label;
        color: $color-blue-dark;
      }
      input {
        line-height: 1.55;
      }
      .group {
        margin: 0 0 35px 0;
        &.teams {
          width: 400px;
        }
        &.name {
          input {
            box-shadow: 0 0 1px 1px rgba(0, 0, 0, .15);
            border-radius: 2px;
            padding: 7px 9px;
            border: 0;
            font-size: $font-medium;
            width: 400px;
          }
        }
      }

      /**
       * Inputs :: Multiselect
       */
      .multiselect__single,
      .multiselect__option,
      .multiselect__input {
        line-height: 1.55;
        font-size: $font-medium;
      }
    }

    .messages {
      margin: 8px 0 30px;
      font-size: $font-small;
      color: $color-gray;

      label {
        @extend %_block-label;
        color: $color-blue-dark;
      }

      &.error {
        color: $color-red-dark;
        label {
          color: $color-red-dark;
        }
        p {
          text-align: center;
        }
      }

      p {
        margin: 0 0 5px;
      }
    }

    .buttons {
      margin: 8px 0 0;
      text-align: center;

      button {
        padding: 12px 60px;
        border-radius: 12px;
        border: 0;
        background-color: rgba($color-red, .5);
        background-image: none !important;
        color: white;
        line-height: 1.55;
        font-weight: bold;
        cursor: pointer;

        &:hover, &:focus {
          background-color: rgba($color-red, .75);
        }
      }
    }

    .help {
      margin: 45px 0 0;

      p {
        @extend %_help_text;
        margin: 0 0 5px 0;

        &::before {
          content: '\00203b ';
        }
      }
    }

    /**
     * Download
     */
    h3 {
      @extend %_block-label;
    }
    .description {
      margin: 0;
      p {
        @extend %_help_text;
        line-height: 1.8;
        text-align: center;
        strong {
          margin: 0 1.5px;
        }
      }
    }
    .download {
      margin: 30px 0 20px;
    }
  }
</style>


<script>
  import url from 'url'
  import log from 'loglevel'
  import VueMultiselect from 'vue-multiselect/src/Multiselect.vue'
  import eventbus from '@/src/eventbus'

  export default {
    props: {
      browser: Object,
      browserExtensionEnabled: Boolean,
      emojiUrl: String,
      visible: Boolean,
    },
    data: () => ({
      progress: false,
      selected: null,
      teams: null,
      selectedTeam: null,
      text: '',

      // Register
      result: {},
      visibleErrors: false,
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

      // Error
      hasErrorMessages() {
        return this.errorMessages.length > 0
      },
      errorMessages() {
        const messages = []
        if (!this.selectedTeam) {
          messages.push(this.$t('Register.messages_validation_team_not_selected_message'))
        }
        if (this.text.length === 0) {
          messages.push(this.$t('Register.messages_validation_no_name_message'))
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

    created() {
      eventbus.$on('EG_EMOJI_GENERATE', () => {
        this.result = {}
        this.text = ''
        this.visibleErrors = false
      })

      // Joined teams received
      this.$ptero.on('CE_SEARCH_JOINED_TEAMS_DONE', ({ detail }) => {
        log.debug('CE_SEARCH_JOINED_TEAMS_DONE', detail)
        if (detail.contents) {
          const teams = [].concat(detail.contents)
          teams.sort((a, b) =>
            a.name < b.name ? -1 :
            a.name > b.name ?  1 : 0) // alphabetical order
          this.teams = teams
        }
      })

      // New emoji registered
      this.$ptero.on('CE_REGISTER_EMOJI_DONE', ({ detail }) => {
        log.debug('CE_REGISTER_EMOJI_DONE', detail)
        this.progress = false
        if (detail.err) {
          if (typeof detail.err !== 'string') {
            this.result = { err: this.$t('Register.messages_failure_unknown_description') }
          } else {
            this.result = detail
          }
        } else {
          this.result = { contents: this.$t('Register.messages_successful_description') }
        }
      })
    },
    methods: {
      onShown() {
        const isEmpty = this.teamsOrEmptyArray.length === 0
        if (this.browserExtensionEnabled && isEmpty) {
          this.$ptero.emit('CE_SEARCH_JOINED_TEAMS')
        }
      },

      updateSelectedTeam(newSelected) {
        this.selectedTeam = newSelected
      },

      // Register
      register() {
        this.visibleErrors = true
        if (this.hasErrorMessages) {
          return
        }

        const args = {
          teamdomain: this.selectedTeam.teamdomain,
          url: url.resolve(location.href, this.emojiUrl),
          text: this.text,
        }
        this.progress = true
        this.result = {}
        this.$ptero.emit('CE_REGISTER_EMOJI', args)

        ga('send', 'event', 'Emoji', 'register')
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
</script>
