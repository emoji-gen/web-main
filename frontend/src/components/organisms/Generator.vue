<template>
  <div class="Generator">
    <!-- Title -->
    <h2 v-t="'Generator.title'"></h2>

    <div class="execution">
      <!-- Button -->
      <button type="button" @click="generate" v-t="'Generator.generate_button'"></button>

      <!-- Public flag -->
      <p class="public-fg" :title="$t('Generator.public_fg_description')">
        <label>
          <input type="checkbox" v-model="publicFg">
          {{ $t('Generator.public_fg_label') }}
        </label>
      </p>
    </div>

    <!-- Parameters -->
    <div class="parameters">
      <!-- Parameter : Text -->
      <div class="parameter text">
        <h3 v-t="'Generator.parameter_text_label'"></h3>
        <textarea rows="2" cols="10" v-model="text"></textarea>

        <h4 v-t="'Generator.parameter_text_align_label'"></h4>
        <div class="aligns">
          <span class="align left">
            <input type="radio" name="Generator__align"
              id="Generator__align--left" value="left" v-model="align">
            <label for="Generator__align--left"></label>
          </span>
          <span class="align center">
            <input type="radio" name="Generator__align"
              id="Generator__align--center" value="center" v-model="align">
            <label for="Generator__align--center"></label>
          </span>
          <span class="align right">
            <input type="radio" name="Generator__align"
              id="Generator__align--right" value="right" v-model="align">
            <label for="Generator__align--right"></label>
          </span>
        </div>

        <h4 v-t="'Generator.parameter_size_label'"></h4>
        <div class="sizes">
          <label>
            <input type="checkbox" v-model="sizeFixed">
            {{ $t('Generator.parameter_size_fixed_label') }}
          </label>
          <label>
            <input type="checkbox" v-model="nonStretch">
            {{ $t('Generator.parameter_size_non_stretch_label') }}
          </label>
        </div>
      </div>

      <!-- Parameter : Font -->
      <div class="parameter font">
        <h3 v-t="'Generator.parameter_font_label'"></h3>
        <ul>
          <li v-for="font in fonts" track-by="$index">
            <input type="radio" name="Generator__font" :value="font.key" :id="'Generator__font--' + font.key" v-model="fontKey">
            <label :for="'Generator__font--' + font.key">{{font.name}}</label>
          </li>
        </ul>
      </div>

      <!-- Parameter : Color -->
      <div class="parameter color">
        <h3 v-t="'Generator.parameter_color_label'"></h3>
        <div class="pickers">
          <div class="picker-wrapper" v-show="colorKind == 'foreground'">
            <ColorPicker v-model="colors" />
          </div>
          <div class="picker-wrapper" v-show="colorKind != 'foreground'">
            <ColorPicker v-model="backgroundColors" />
          </div>
        </div>
        <ColorKind @change="colorKindChanged" />
      </div>
    </div>
  </div>
</template>


<style lang="scss" scoped>
  @import 'includes/_variables';
  @import 'includes/_mixins';

  %_parameter {
    box-shadow: 0 0 1px 1px rgba(0, 0, 0, .15);
    border-radius: 2px;
  }

  .Generator {
    @extend %box;
    padding: 20px 0 35px;
    line-height: 1.55;

    &, * {
      box-sizing: border-box;
    }

    /* Title */
    h2 {
      @extend %box-heading;
    }

    /**
     * Execution
     */
    .execution {
      margin: 40px 0 0 0;
      text-align: center;

      /* Button */
      button {
        padding: 12px 60px;
        border: 0;
        border-radius: 12px;
        line-height: 1.55;
        background-color: rgba($color-red, .5);
        background-image: none !important;
        color: white;
        font-weight: bold;
        cursor: pointer;

        &:hover, &:focus {
          background-color: rgba($color-red, .75);
        }
      }

      /* Public flag */
      > .public-fg {
        color: $color-gray;
        letter-spacing: .4px;
        font-size: $font-xsmall;

        label {
          padding: 0 3px;

          input {
            margin-right: 3px;
          }
        }
      }
    }

    /*
     * Parameters
     */
    .parameters {
      display: flex;
      justify-content: center;
      margin: 38px 0 0;

      h3 {
        display: block;
        margin: 0 0 16px;
        font-size: $font-medium;
        font-weight: bold;
        letter-spacing: 1px;
        text-align: center;
      }
      h4 {
        display: block;
        margin: 0 0 10px;
        font-size: $font-small;
        font-weight: bold;
        letter-spacing: 1px;
        text-align: center;
      }

      .parameter {
        margin: 0 30px 0;
        text-align: center;

        h3 {
          color: $color-blue-dark;
        }
        h4 {
          color: $color-gray;
        }

        /**
         * Parameter : Text
         */
        &.text {
          display: flex;
          flex-direction: column;
          align-items: center;

          textarea {
            @extend %_parameter;
            margin: 0 0 24px 0;
            padding: 10px;
            border: 0;
            width: 140px;
            height: 100px;
            line-height: 1.55;
            text-align: center;
            -webkit-appearance: none;
          }

          /**
           * Parameter : Text : Align
           */
          .aligns {
            display: flex;
            justify-content: space-between;
            width: 98px;
            margin: -1px 0 24px;

            .align {
              $_size: 20px;
              display: inline-block;
              position: relative;
              width: $_size;
              height: $_size;
              label {
                position: absolute;
                top: 0;
                right: 0;
                bottom: 0;
                left: 0;
                overflow: hidden;
                padding-top: $_size;
                background-size: $_size, 0;
                background-repeat: no-repeat;
                cursor: pointer;
              }
              input {
                display: none;
              }
              input:checked + label {
                background-size: 0, $_size;
              }
              &.left {
                label {
                  background-image:
                    url($site-url + '/assets/img/align_left.png'),
                    url($site-url + '/assets/img/align_left_active.png');
                }
              }
              &.center {
                label {
                  background-image:
                    url($site-url + '/assets/img/align_center.png'),
                    url($site-url + '/assets/img/align_center_active.png');
                }
              }
              &.right {
                label {
                  background-image:
                    url($site-url + '/assets/img/align_right.png'),
                    url($site-url + '/assets/img/align_right_active.png');
                }
              }
            }
          }

          /**
           * Parameter : Text : Size
           */
          .sizes {
            display: flex;
            flex-direction: column;
            line-height: 1;
            color: $color-gray;
            text-align: left;
            font-size: $font-xsmall;

            label {
              display: block;
              cursor: pointer;

              &:first-of-type {
                margin-bottom: 6px;
              }
              input {
                margin-right: 2px;
              }
            }
          }
        }

        /**
         * Parameter : Color
         */
        &.color {
          margin-right: 32px;
          .picker-wrapper {
            > div {
              @extend %_parameter;
              margin-bottom: 8px;
            }
          }
        }

        /**
         * Parameter : Font
         */
        &.font {
          ul {
            margin: 0;
            padding: 0;
            list-style-type: none;
            list-style-position: inside;
          }
          input {
            display: none;

            &:checked + label {
              border: 1px solid rgba(darken($color-blue, 20%), .8);
              background-image: url($site-url + '/assets/img/checked.png');
              background-repeat: no-repeat;
              background-position: 14px center;
              background-size: 20px auto;
              color: darken($color-blue, 20%);
            }
          }

          label {
            display: block;
            margin: 0 0 5px;
            padding: 8px 23px 8px 46px;
            border-radius: 16px;
            border: 1px solid rgba(0, 0, 0, .2);
            color: rgba(0, 0, 0, .32);
            font-size: $font-medium;
            text-align: left;
            user-select: none;
            cursor: pointer;
          }
        }
      }
    }
  }

</style>


<script>
  import Chrome from 'vue-color/src/components/Chrome'
  import SweetScroll from 'sweet-scroll'
  import eventbus from '@/src/eventbus'
  import { FONTS, LOCALE } from '@/src/initial_state'
  import { getLocale, toLocalizedPath } from '@/src/locales'

  const DEFAULT_COLORS = {
    hex: '#EC71A1',
    rgba: {
      r: 236,
      g: 113,
      b: 161,
      a: 1
    },
    a: 1
  }

  const DEFAULT_BACKGROUND_COLORS = {
    hex: '#FFFFFF',
    rgba: {
      r: 255,
      g: 255,
      b: 255,
      a: 0
    },
    a: 0
  }

  export default {
    data: () => ({
      // Parameters
      text: null,
      align: 'center',
      sizeFixed: false,
      nonStretch: false,
      publicFg: true,

      // Font
      fontKey: FONTS[LOCALE][0].key,
      locale: LOCALE,

      // Colors
      colorKind: 'foreground',
      colors: DEFAULT_COLORS,
      backgroundColors: DEFAULT_BACKGROUND_COLORS,
    }),
    computed: {
      fonts() {
        return FONTS[this.locale]
      },
    },
    created() {
      this.text = this.$t('Generator.parameter_text_default_value')
    },
    methods: {
      generate() {
        const color = this.colorsToRgbaHex(this.colors)
        const backgroundColors = this.colorsToRgbaHex(this.backgroundColors)

        const query = {
          text: this.text,
          color,
          back_color: backgroundColors,
          font: this.fontKey,
          size_fixed: this.sizeFixed,
          align: this.align,
          stretch: !this.nonStretch,
          public_fg: this.publicFg,
          locale: this.locale,
        }

        eventbus.$emit('EG_EMOJI_GENERATE', query)
        this.$router.replace({
          path: toLocalizedPath('/result'),
          query,
        })

        const scroller = new SweetScroll({ easing: 'easeOutQuad' })
        scroller.toTop(0)
      },
      colorsToRgbaHex(colors) {
        const rgb = colors.hex.replace(/#/, '')
        const alphaInt = Math.floor(colors.a * 0xff) & 0xff
        const alpha = ('0' + alphaInt.toString(16)).slice(-2).toUpperCase()
        return rgb + alpha
      },
      colorKindChanged(value){
        this.colorKind = value
      },
    },

    components: {
      ColorPicker: Chrome,
    },
  }
</script>

