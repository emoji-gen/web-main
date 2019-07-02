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
          />
        </div>
        <div class="group name">
          <label v-t="'Register.inputs_name_label'"></label>
          <input type="text" :placeholder="$t('Register.inputs_name_placeholder')"
            v-model="text" @keypress="registerByKeyPress">
        </div>
      </div>

      <div class="messages error" v-if="visibleErrors && hasErrorMessages">
        <label v-t="'Register.messages_error'"></label>
        <p v-for="errorMessage in errorMessages">{{ errorMessage }}</p>
      </div>

      <div class="messages" v-if="result.contents">
        <label>絵文字を登録しました！</label>
        <p>{{ result.contents }}</p>
      </div>

      <div class="messages error" v-if="result.err">
        <label>絵文字の登録に失敗しました</label>
        <p>{{ result.err }}</p>
      </div>

      <div class="buttons">
        <button type="button" @click="register" v-t="'Register.register_button'"></button>
      </div>

      <div class="help">
        <p>ブラウザでログイン中の Slack チームが一覧に表示されます</p>
        <p>登録したいチームが表示されない場合、該当のチームへ<a href="https://slack.com/signin" target="_blank" rel="nofollow noopener">ログイン</a>してください</p>
      </div>
    </div>

    <div class="inner" v-else>
      <h3>ブラウザ拡張機能をインストールしてください</h3>
      <div class="description">
        <p>
          ブラウザ拡張機能をインストールすると、<br>
          Slack チームへ絵文字を<strong>直接登録</strong>することができます。
        </p>
      </div>

      <div class="download">
        <a href="https://chrome.google.com/webstore/detail/%E7%B5%B5%E6%96%87%E5%AD%97%E3%82%B8%E3%82%A7%E3%83%8D%E3%83%AC%E3%83%BC%E3%82%BF%E3%83%BC/ghbhakkknnmocmiilhneahbkiaegdnmf?hl=ja&amp;gl=JP" target="_blank" v-if="browser.name == 'chrome'">
          <img src="/assets/img/chrome_web_store.png" width="248" height="75" alt="available in the chrome web store">
        </a>
        <a href="https://addons.mozilla.org/ja/firefox/addon/emoji-generator/" target="_blank" v-if="browser.name == 'firefox'">
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
      background-image: url('/assets/img/loading_red.gif');
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
      eventbus.$on('CE_SEARCH_JOINED_TEAMS_DONE', detail => {
        if (detail.contents) {
          const teams = [].concat(detail.contents)
          teams.sort((a, b) =>
            a.name < b.name ? -1 :
            a.name > b.name ?  1 : 0) // alphabetical order
          this.teams = teams
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
        console.log(newSelected)
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
