<template>
  <div class="Contact">
    <h2>お問い合わせ</h2>
    <div class="body">
      <p>要望・不具合報告などは、GitHub で新規に Issue を作成してください。</p>
      <ul>
        <li class="github">
          <a href="https://github.com/emoji-gen/web-main/issues" target="_blank">
            <span class="owner">emoji-gen</span>/<span class="username">web-main</span>
          </a>
        </li>
      </ul>

      <p class="break">その他のお問い合わせは、公式 Twitter までお願いします。</p>
      <ul>
        <li class="twitter">
          <a href="https://twitter.com/emoji_gen" target="_blank" rel="noopener">@emoji_gen</a>
        </li>
      </ul>
    </div>
  </div>
</template>


<style lang="scss" scoped>
  @import 'includes/_variables';
  @import 'includes/_mixins';

  .Contact {
    @extend %box;
    padding: 32px 32px (32px + 28px) 32px;
    margin-bottom: 180px;
    min-height: 600px;

    &, * {
      box-sizing: border-box;
    }
    h2 {
      @extend %box-heading;
    }

    .body {
      padding: 30px;

      ul {
        margin: 18px 0;

        li {
          margin: 10px 0;
          padding: 1px 0 0 42px;
          height: 30px;
          line-height: 30px;
          list-style-type: none;
          list-style-position: inside;
          background-size: 26px auto;
          background-repeat: no-repeat;
          background-position: 0 center;
          font-size: $font-medium;

          a {
            text-decoration: none;

            .owner {
              margin-right: 2px;
            }

            .username {
              margin-left: 2.5px;
            }
          }

          &.twitter { @extend %icon-26px-twitter }
          &.github { @extend %icon-40px-github }
        }
      }
    }
  }
</style>


<script>
  import { CONTACT_TITLE } from '@/src/initial_state'

  export default {
    mounted() {
      document.title = CONTACT_TITLE
    },
  }
</script>
