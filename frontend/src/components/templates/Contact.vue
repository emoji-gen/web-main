<template>
  <div class="Contact">
    <DocumentTitle :value="$t('Contact.title')" />
    <h2 v-t="'Contact.heading'"></h2>
    <div class="body">
      <p v-t="'Contact.github_issue_description'"></p>
      <ul>
        <li class="github">
          <a href="https://github.com/emoji-gen/web-main/issues" target="_blank" rel="noopener">
            <span class="owner">emoji-gen</span>/<span class="username">web-main</span>
          </a>
        </li>
      </ul>

      <p class="break" v-t="'Contact.twitter_description'"></p>
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
      font-size: $font-medium;

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
          &.github { @extend %icon-26px-github }
        }
      }
      p {
        &.break {
          margin-top: 45px;
        }
      }
    }
  }
</style>


<script>
  export default {
  }
</script>
