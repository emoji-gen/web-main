<template>
  <div class="Generator">
    <!-- Title -->
    <h2>絵文字にしたい文字を入力してください！</h2>

    <div class="execution">
      <!-- Button -->
      <button type="button" @click="generate">生成する&#9834;</button>

      <!-- Public flag -->
      <p class="public-fg" title="チェックマークを外すと、絵文字が生成履歴に残りません。">
        <label class="pure-checkbox">
          <input type="checkbox" v-model="publicFg">
          生成履歴に絵文字を表示する
        </label>
      </p>
    </div>

    <!-- Parameters -->
    <div class="parameters">
      <!-- Parameter : Text -->
      <div class="parameter text">
        <h3>テキスト</h3>
        <textarea rows="2" cols="10"></textarea>

        <h4>文字揃え</h4>
        <div class="aligns">
          <span class="align left">
            <input type="radio" name="Generator__align" id="Generator__align--left" value="left">
            <label for="Generator__align--left">左</label>
          </span>
          <span class="align center">
            <input type="radio" name="Generator__align" id="Generator__align--center" value="center">
            <label for="Generator__align--center">中央</label>
          </span>
          <span class="align right">
            <input type="radio" name="Generator__align" id="Generator__align--right" value="right">
            <label for="Generator__align--right">右</label>
          </span>
        </div>

        <h4>サイズ調整</h4>
        <div class="sizes">
          <label>
            <input type="checkbox">
            文字サイズを固定する
          </label>
          <label>
            <input type="checkbox">
            自動で伸縮しない
          </label>
        </div>
      </div>

      <!-- Parameter : Font -->
      <div class="parameter font">
        <h3>フォント</h3>
        <ul>
          <li v-for="font in fonts" track-by="$index">
            <input type="radio" name="Generator__font" :value="font.key" :id="'Generator__font--' + font.key" v-model="fontKey">
            <label :for="'Generator__font--' + font.key">{{font.name}}</label>
          </li>
        </ul>
      </div>


      <!-- Parameter : Color -->
      <ColorPicker v-model="colors" />
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
        line-height: normal;
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
                  background-image: url('/assets/img/align_left.png'), url('/assets/img/align_left_active.png');
                }
              }
              &.center {
                label {
                  background-image: url('/assets/img/align_center.png'), url('/assets/img/align_center_active.png');
                }
              }
              &.right {
                label {
                  background-image: url('/assets/img/align_right.png'), url('/assets/img/align_right_active.png');
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
              background-image: url(/assets/img/checked.png);
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
  import get from 'lodash.get'
  import { mapState } from 'vuex'
  import { Chrome } from 'vue-color'

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

  const FONTS = window.GENERATOR_FONTS || []

  export default {
    data: () => ({
      publicFg: true,
      fonts: FONTS,
      fontKey: get(FONTS, '[0].key'),
      colors: DEFAULT_COLORS,
    }),
    methods: {
      generate() {
        console.log('generate')
      },
    },
    components: {
      ColorPicker: Chrome,
    },
  }
</script>

