<template>
  <div class="HeaderTitle">
    <h1><a :href="homePath" v-t="'Header.title'"></a></h1>
  </div>
</template>


<style lang="scss" scoped>
  @import 'includes/_variables';
  @import 'includes/_mixins';

  $_height: 74px;
  $_logo-size: 40px;
  $_color: rgb(80, 80, 80);
  $_rotate: -18deg;

  .HeaderTitle {
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

        &:lang(en) {
          padding: 0 0 0 88px;
        }

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
          background-size: $_logo-size auto;
          background-repeat: no-repeat;
          background-position: 0px center;
          content: '';
        }
        &:lang(en) {
          &::before {
            background-image: url($site-url + '/assets/img/logo_en-40x40@1x.png');
            background-image: image-set(
              $site-url + '/assets/img/logo_en-40x40@1x.png' 1x,
              $site-url + '/assets/img/logo_en-40x40@2x.png' 2x);
          }
        }
        &:lang(ja) {
          &::before {
            background-image: url($site-url + '/assets/img/logo_ja-40x40@1x.png');
            background-image: image-set(
              $site-url + '/assets/img/logo_ja-40x40@1x.png' 1x,
              $site-url + '/assets/img/logo_ja-40x40@2x.png' 2x);
          }
        }
        &:lang(ko) {
          &::before {
            background-image: url($site-url + '/assets/img/logo_ko-40x40@1x.png');
            background-image: image-set(
              $site-url + '/assets/img/logo_ko-40x40@1x.png' 1x,
              $site-url + '/assets/img/logo_ko-40x40@2x.png' 2x);
          }
        }
      }
    }
  }
</style>


<script>
  import eventbus from '@/src/eventbus'
  import { toLocalizedPath } from '@/src/locales'

  export default {
    data: () => ({
      homePath: toLocalizedPath('/'),
    }),

    created() {
      eventbus.$on('EG_LOCALE_CHANGED', () => {
        this.homePath = toLocalizedPath('/')
      })
    },
  }
</script>

