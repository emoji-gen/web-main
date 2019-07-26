<template>
  <div class="Result">
    <transition name="expand">
      <div class="result-inner" v-show="visibleResult">
        <!-- Title -->
        <h2>{{ $t('Result.title') }}</h2>

        <!-- Preview -->
        <div class="preview">
          <div class="preview-inner">
            <div class="image">
              <img :src="emojiUrl" alt="" v-if="emojiUrl">
            </div>
            <div class="detail">
              <ul>
                <li class="text">
                  <h3 v-t="'Result.preview_text_label'"></h3>
                  <span class="user-input">{{ formattedText }}</span>
                </li>
                <li class="font">
                  <h3 v-t="'Result.preview_font_label'"></h3>
                  <span class="user-input">{{ fontName }}</span>
                </li>
                <li class="color">
                  <h3 v-t="'Result.preview_color_label'"></h3>
                  <span class="user-input">
                    <span class="color-square" v-bind:style="{ backgroundColor: cssColor }"></span>
                    {{ cssColor }}
                  </span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Menus -->
        <div class="menus">
          <div class="menus-inner">
            <div class="download">
              <a :href="emojiDownloadUrl" @click="download" v-t="'Result.menus_download_label'"></a>
            </div>
            <div class="register" @click="toggleRegister"
              v-show="visibleRegisterButton" v-t="'Result.menus_register_label'"></div>
            <div class="share" @click="toggleShare" v-t="'Result.menus_share_label'"></div>
          </div>
        </div>

        <!-- Register -->
        <transition name="register">
          <Register
            :visible="visibleRegister"
            :browser="browser"
            :browser-extension-enabled="browserExtensionEnabled"
            :emoji-url="emojiDownloadUrl"
            v-show="visibleRegister" />
        </transition>

        <!-- Share -->
        <transition name="share">
          <Share
            :visible="visibleShare"
            :emoji-url="emojiDownloadUrl"
            v-show="visibleShare" />
        </transition>
      </div>
    </transition>
  </div>
</template>


<style lang="scss">
  @import 'includes/_variables';
  @import 'includes/_mixins';

  .Result {
    line-height: 1.55;

    &, * {
      box-sizing: border-box;
    }

    /**
     * Transition
     */
    .result-inner {
      @extend %box;
      padding: 20px;
    }
    .expand-enter {
      padding: 0;
      height: 0;
      overflow: hidden;
      opacity: 0;
    }
    .expand-enter-to {
      opacity: 1;
      transition: opacity .8s ease-in-out;
    }

    /**
     * Title
     */
    h2 {
      @extend %box-heading;
    }

    /**
     * Preview
     */
    .preview {
      display: flex;
      margin: 30px auto 0;
      justify-content: center;

      .preview-inner {
        display: flex;
        align-items: stretch;

        /**
         * Preview : Image
         */
        .image {
          $_border-width: 1px;
          display: block;
          width: ($dimen-emoji-size + $_border-width * 2);
          height: ($dimen-emoji-size + $_border-width * 2);
          border-radius: 5px;
          background-color: rgba(255, 255, 255, .38);

          img {
            box-sizing: content-box;
            width: $dimen-emoji-size;
            height: $dimen-emoji-size;
            border: 1px solid rgba(0, 0, 0, .18);
            border-radius: 5px;
          }
        }

        /**
         * Preview : Detail
         */
        .detail {
          display: flex;
          flex-direction: column;
          justify-content: center;
          margin: 0 0 0 50px;

          ul {
            $_height: 40px;
            margin: 0;
            padding: 0;
            list-style-type: none;
            list-style-position: inside;

            li {
              display: flex;
              line-height: $_height;

              h3 {
                margin: 0;
                width: 68px;
                color: $color-blue-dark;
                font-weight: bold;
                font-size: $font-medium;
              }

              &::before {
                display: block;
                float: left;
                margin-right: 10px;
                width: 30px;
                height: $_height;
                background-repeat: no-repeat;
                background-position: center center;
                content: '';
                opacity: .8;
              }
              &.text {
                &::before {
                  background-image: url($site-url + '/assets/img/text.png');
                  background-size: 28px auto;
                  opacity: .80;
                }
              }
              &.font {
                &::before {
                  background-image: url($site-url + '/assets/img/font.png');
                  background-size: 25px auto;
                  opacity: .80;
                }
              }
              &.color {
                &::before {
                  background-image: url($site-url + '/assets/img/color.png');
                  background-size: 19px auto;
                  opacity: .80;
                }
              }
              .user-input {
                display: block;
                margin: 0 0 0 12px;
                color: rgba(0, 0, 0, .75);
                font-size: $font-small;

                > .color-square {
                  display: inline-block;
                  margin: 1px 4px 0 0;
                  border: 1px solid rgba(0, 0, 0, .18);
                  width: 10px;
                  height: 10px;
                }
              }
            }
          }
        }
      }
    }

    /**
     * Menus
     */
    .menus {
      $_height: 40px;
      display: flex;
      margin: 30px auto 15px;
      justify-content: center;

      .menus-inner {
        display: flex;

        > div {
          margin-left: 40px;
          padding: 0;
          height: $_height;
          line-height: $_height;
          font-size: $font-medium;

          &:first-child {
            margin-left: 0;
          }

          a {
            display: block;
            text-decoration: none;
          }

          &.download {
            a {
              padding: 0 0 0 34px;
              color: $color-red-dark;
              height: 100%;
              background-image: url($site-url + '/assets/img/download-22x22@1x.png');
              background-image: image-set(
                $site-url + '/assets/img/download-22x22@1x.png' 1x,
                $site-url + '/assets/img/download-22x22@2x.png' 2x);
              background-repeat: no-repeat;
              background-position: 0 center;
              background-size: 22px auto;
              cursor: pointer;
            }
          }

          &.register {
            padding: 0 0 0 34px;
            color: $color-red-dark;
            height: 100%;
            background-image: url($site-url + '/assets/img/register-22x22@1x.png');
            background-image: image-set(
              $site-url + '/assets/img/register-22x22@1x.png' 1x,
              $site-url + '/assets/img/register-22x22@2x.png' 2x);
            background-repeat: no-repeat;
            background-position: 0 center;
            background-size: 22px auto;
            cursor: pointer;
          }

          &.share {
            padding: 0 0 0 34px;
            color: $color-yellow-dark;
            background-image: url($site-url + '/assets/img/share.png');
            background-repeat: no-repeat;
            background-position: 0 center;
            background-size: 22px auto;
            cursor: pointer;
          }
        }
      }
    }

    /**
     * Register, Share
     */
    .register-enter, .share-enter {
      padding: 0;
      height: 0;
      overflow: hidden;
      opacity: 0;
    }
    .register-enter-to, .share-enter-to {
      opacity: 1;
      transition: opacity .8s ease-in-out;
    }
  }
</style>


<script>
  import queryString from 'query-string'
  import { detect } from 'detect-browser'
  import loglevel from 'loglevel'

  import eventbus from '@/src/eventbus'
  import { FONTS } from '@/src/initial_state'

  export default {
    data: () => ({
      // URL
      queryString: null,

      // Parameters
      color: null,
      fontKey: null,
      text: null,
      queryLocale: null,

      // Browser extension
      browser: detect(),
      browserExtensionEnabled: false,

      visibleResult: false,
      visibleRegister: false,
      visibleShare: false,
    }),
    computed: {
      // URL
      emojiUrl: function () {
        if (this.queryString) {
          return `/emoji?${this.queryString}`
        }
        return null
      },
      emojiDownloadUrl: function () {
        if (this.queryString) {
          return `/emoji_download?${this.queryString}`
        }
        return null
      },

      // Parameters
      formattedText() {
        if (!this.text) {
          return ''
        }
        return this.text.replace(/\n/,' ')
      },
      fontName() {
        if (!this.fontKey) {
          return ''
        }

        const font = FONTS[this.queryLocale].find(v => v.key === this.fontKey)
        if (!font) {
          return ''
        }
        return font.name
      },
      cssColor() {
        if (this.color) {
          return `#${this.color.slice(0, 6)}`
        }
        return ''
      },

      // Browser extension
      isRegisterSupportedBrowser() {
        return this.browser.name === 'chrome' || this.browser.name === 'firefox'
      },
      visibleRegisterButton() {
        return this.browserExtensionEnabled || this.isRegisterSupportedBrowser
      },
    },
    created() {
      // Initial state
      if (this.$route.path.match(/^(?:\/[a-zA-Z-]+)?\/result/)) {
        this._draw(this.$route.query)
      }

      // A new emoji generated
      eventbus.$on('EG_EMOJI_GENERATE', query => {
        this._draw(query)
      })

      // Browser extension attached
      this.$ptero.on('CE_ATTACH', () => {
        this.browserExtensionEnabled = true
      })
    },
    methods: {
      _draw(query) {
        loglevel.debug('A new emoji generated', query)

        this.text = query.text
        this.color = query.color
        this.fontKey = query.font
        this.queryLocale = query.locale
        this.queryString = queryString.stringify(query)
        this.visibleResult = true
        this.visibleRegister = false
      },

      download() {
        ga('send', 'event', 'Emoji', 'download')
      },
      toggleShare() {
        if (this.visibleShare) {
          this.visibleShare = false
        } else {
          this.visibleShare = true
          this.visibleRegister = false
        }
      },
      toggleRegister() {
        if (this.visibleRegister) {
          this.visibleRegister = false
        } else {
          this.visibleRegister = true
          this.visibleShare = false
        }
      },
    },
  }
</script>
