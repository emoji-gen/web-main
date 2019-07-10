<template>
  <div class="Share">
    <div class="inner">
      <input
        type="button"
        class="twitter sharer button"
        data-sharer="twitter"
        :data-title="tweet"
        :title="$t('Share.twitter_description')"
        v-sharer>

      <input
        type="button"
        class="facebook sharer button"
        data-sharer="facebook"
        :data-url="url"
        :title="$t('Share.facebook_description')"
        v-sharer>

      <input
        type="button"
        class="line sharer button"
        data-sharer="line"
        :data-title="$t('Share.line_message')"
        :data-url="url"
        :title="$t('Share.line_description')"
        v-sharer>
    </div>
  </div>
</template>


<style lang="scss">
  @import 'includes/_variables';
  @import 'includes/_mixins';

  .Share {
    padding: 20px 0 20px;

    .inner {
      display: flex;
      flex: 1 1 auto;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      transition: opacity .8s ease-in-out;
      opacity: 1;

      input {
        @extend %icon-40px;
        margin: 0 0 0 20px;
        cursor: pointer;

        &.twitter {
          @extend %icon-40px-twitter;
          margin-left: 0;
        }
        &.facebook {
          @extend %icon-40px-facebook;
        }
        &.line {
          @extend %icon-40px-line;
        }
      }
    }
  }
</style>


<script>
  import VueSharer from 'vue-sharer'

  export default {
    computed: {
      tweet: {
        cache: false,
        get() {
          return this.$t('Share.twitter_tweet') + ' ' +
            location.href + ' ' + this.$t('Share.twitter_hashtag')
        },
      },
      url: {
        cache: false,
        get() {
          return location.href
        },
      },
    },
    directives: {
      sharer: VueSharer,
    },
  }
</script>
