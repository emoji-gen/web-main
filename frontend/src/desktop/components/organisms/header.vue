<template>
  <div class="v-cloak eg-header">
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
        <input type="button" class="google sharer button" data-sharer="googleplus" data-url="https://emoji.pine.moe/" title="Google+ でシェアする" v-sharer>
        <a href="https://github.com/emoji-gen/Emoji-Web" class="github" target="_blank">GitHub</a>
      </div>
    </header>
  </div>
</template>

<script>
  import VueSharer from 'vue-sharer'
  export default {
    directives: {
      sharer: VueSharer,
    },
  }
</script>

<style lang="scss" scoped>
  @import "desktop/style/_variables";

  .eg-header {
    z-index: 1;
    //height: $_height;
   // background-color: $background-color-white;
    //box-shadow: 0px 0px 3px 1px $bar-box-shadow-color;
  }


</style>
