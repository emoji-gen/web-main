<template>
  <div class="v-cloak Header" :class="{ webp: supportsWebP }">
    <header>
      <h1><a href="/">絵文字 ジェネレーター</a></h1>
      <div class="icons">
        <input
          type="button"
          class="twitter sharer button"
          data-sharer="twitter"
          data-title="絵文字ジェネレーター使ってます♪"
          data-hashtags="絵文字ジェネレーター"
          data-url="https://emoji-gen.ninja"
          title="Twitter でシェアする"
          v-sharer>

        <input
          type="button"
          class="facebook sharer button"
          data-sharer="facebook"
          data-url="https://emoji-gen.ninja"
          title="Facebook でシェアする"
          v-sharer>

        <input
          type="button"
          class="google sharer button"
          data-sharer="googleplus"
          data-url="https://emoji-gen.ninja"
          title="Google+ でシェアする"
          v-sharer>

        <a href="https://github.com/emoji-gen/web-main" class="github" target="_blank" rel=noopener>GitHub</a>
      </div>
    </header>
  </div>
</template>


<script>
  import VueSharer from 'vue-sharer'
  import { mapState } from 'vuex'

  export default {
    computed: {
      supportsWebP() {
        return this.$store.state.browser.supportsWebP
      },
    },

    directives: {
      sharer: VueSharer,
    },
  }
</script>


<style lang="scss" scoped>
  @import "desktop/style/_variables";

  $_height: $dimen-header-height;
  $_width: $dimen-content-width;
  $_margin-left-right: 20px;
  $_color: rgb(80, 80, 80);
  $_logo-size: 40px;

  .Header {
    z-index: 1;
    height: $_height;
    background-color: $background-color-white;
    box-shadow: 0px 0px 3px 1px $bar-box-shadow-color;

    &, * {
      box-sizing: border-box;
    }

    header {
      display: flex;
      margin: 0 auto;
      padding: 0;
      width: $_width;
      height: $_height;

      h1 {
        position: relative;
        display: block;
        margin: 0;
        padding: 0;

        a {
          display: block;
          margin: 0;
          padding: 0 0 0 ($_margin-left-right + 60px);
          line-height: $_height;
          letter-spacing: 6px;
          color: $_color;
          text-decoration: none;
          font-size: $font-size-xlarge;
          font-weight: bold;

          &::before {
            display: block;
            position: absolute;
            top: 0;
            bottom: 0;
            left: $_margin-left-right;
            right: 0;
            width: $_logo-size;
            transform: rotate($slack-rotate-left);
            background-image: url('/assets/img/logo.png');
            background-size: $_logo-size auto;
            background-repeat: no-repeat;
            background-position: 0px center;
            content: '';
          }
        }
      }
    }

    &.webp header h1 a {
      &::before {
        background-image: url('/assets/img/logo.webp');
      }
    }
  }

</style>
