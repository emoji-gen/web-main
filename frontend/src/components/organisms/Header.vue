<template>
  <div class="Header">
    <header>
      <!-- Logo + Title -->
      <h1><a href="/">絵文字 ジェネレーター</a></h1>

      <!-- Buttons -->
      <div class="buttons">
        <a href="https://twitter.com/emoji_gen" class="twitter" target="_blank" title="絵文字ジェネレーター 公式 Twitter" rel="noopener">Twitter</a>
        <a href="https://github.com/emoji-gen/web-main" class="github" target="_blank" rel="noopener">GitHub</a>
      </div>
    </header>
  </div>
</template>


<style lang="scss">
  @import 'includes/_variables';
  @import 'includes/_mixins';

  $_width: $dimen-content-width;
  $_height: 74px;
  $_logo-size: 40px;
  $_color: rgb(80, 80, 80);
  $_rotate: -18deg;

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

      /* Logo + Text */
      h1 {
        position: relative;
        display: block;
        margin: 0;
        padding: 0;

        a {
          display: block;
          margin: 0;
          padding: 0 0 0 80px;
          line-height: $_height;
          letter-spacing: 6px;
          color: $_color;
          text-decoration: none;
          font-size: $font-xlarge;
          font-weight: bold;

          /* Logo */
          &::before {
            display: block;
            position: absolute;
            top: 0;
            bottom: 0;
            left: 20px;
            right: 0;
            width: $_logo-size;
            transform: rotate($_rotate);
            background-image: url('/assets/img/logo.png');
            background-size: $_logo-size auto;
            background-repeat: no-repeat;
            background-position: 0px center;
            content: '';
          }
        }
      }

      /* Buttons */
      .buttons {
        display: flex;
        flex: 1 1 auto;
        flex-direction: row;
        justify-content: flex-end;
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
