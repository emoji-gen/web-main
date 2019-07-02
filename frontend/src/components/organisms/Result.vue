<template>
  <div class="Result">
    <!-- Title -->
    <h2 v-t="'Result.title'"></h2>

    <!-- Preview -->
    <div class="preview">
      <div class="inner">
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
  </div>
</template>


<style lang="scss" scoped>
  @import 'includes/_variables';
  @import 'includes/_mixins';

  .Result {
    @extend %box;
    padding: 20px;
    line-height: 1.55;

    &, * {
      box-sizing: border-box;
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

      > .inner {
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
                  background-image: url('/assets/img/text.png');
                  background-size: 28px auto;
                  opacity: .80;
                }
              }
              &.font {
                &::before {
                  background-image: url('/assets/img/font.png');
                  background-size: 25px auto;
                  opacity: .80;
                }
              }
              &.color {
                &::before {
                  background-image: url('/assets/img/color.png');
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
  }
</style>


<script>
  import queryString from 'query-string'
  import loglevel from 'loglevel'

  import eventbus from '@/src/eventbus'
  import { FONTS } from '@/src/initial_state'

  export default {
    data: () => ({
      // URL
      queryString: null,

      // Parameters
      color: null,
      fonts: FONTS,
      fontKey: null,
      text: null,

      // Browser extension
      browserExtensionEnabled: false,
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

        const font = this.fonts.find(v => v.key === this.fontKey)
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
    },
    created() {
      // Initial state
      if (this.$route.path.indexOf('/result') === 0) {
        this.$nextTick(() => {
          this.draw(this.$route.query)
        })
      }

      // A new emoji generated
      eventbus.$on('EG_EMOJI_GENERATE', query => {
        this.draw(query)
      })

      // Browser extension attached
      eventbus.$on('CE_ATTACH', () => {
        this.browserExtensionEnabled = true
      })
    },
    methods: {
      draw(query) {
        loglevel.debug('A new emoji generated', query)

        this.text = query.text
        this.color = query.color
        this.fontKey = query.font
        this.queryString = queryString.stringify(query)
        this.visibleResult = true
        this.visibleRegister = false
      },
    },
  }
</script>
