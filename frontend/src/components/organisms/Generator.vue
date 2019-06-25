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
    </div>
  </div>
</template>


<style lang="scss" scoped>
  @import 'includes/_variables';
  @import 'includes/_mixins';

  .Generator {
    @extend %box;
    padding: 20px 0 35px;

    &, * {
      box-sizing: border-box;
    }

    /* Title */
    h2 {
      @extend %box-heading;
    }

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

  }

</style>


<script>
  export default {
    data: () => ({
      publicFg: true,
    }),
    methods: {
      generate() {
        console.log('generate')
      },
    },
  }
</script>

