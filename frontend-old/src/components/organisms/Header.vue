<template>
  <div class="Header">
    <header>
      <!-- Logo + Title -->
      <HeaderTitle />

      <!-- Language -->
      <HeaderLanguage />

      <!-- Buttons -->
      <div class="buttons">
        <!-- Buttons : Twitter -->
        <a href="https://twitter.com/emoji_gen"
          class="twitter"
          target="_blank"
          rel="noopener"></a>

        <!-- Buttons : GitHub -->
        <a href="https://github.com/emoji-gen/web-main"
          class="github"
          target="_blank"
          rel="noopener"></a>
      </div>
    </header>
  </div>
</template>


<style lang="scss" scoped>
  @import 'includes/_variables';
  @import 'includes/_mixins';

  $_width: $dimen-content-width;
  $_height: 74px;

  .Header {
    z-index: 1;
    height: $_height;
    line-height: 1.55;
    background-color: $color-background-white;
    box-shadow: 0px 0px 3px 1px $color-shadow-white;

    &, * {
      box-sizing: border-box;
    }

    header {
      display: flex;
      margin: 0 auto;
      padding: 0;
      width: $_width;
      height: $_height;

      /* Buttons */
      .buttons {
        display: flex;
        flex-direction: row;
        align-items: center;
        margin: 0 20px 0 0;

        input, a {
          @extend %icon-40px;
          margin: 0 0 0 12px;

          &.github {
            @extend %icon-40px-github;
          }
          &.twitter {
            @extend %icon-40px-twitter;
          }
        }
      }
    }
  }
</style>
