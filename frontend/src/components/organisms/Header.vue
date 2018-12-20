<template>
  <div class="Header">
    <!-- <h1><a href="/">絵文字 ジェネレーター</a></h1> -->
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
  </div>
</template>


<style lang="scss" scoped>
</style>


<script>
  export default {
  }
</script>

