<template>
  <div class="Footer">
    <footer>
      <!-- Menus-->
      <ul class="menus">
        <li><a href="/blog/" target="_blank" v-t="'Footer.developer_blog_label'"></a></li>
        <li><router-link to="/contact" @click.native="scroll" v-t="'Footer.contact_label'" /></li>
      </ul>

      <!-- Copyright -->
      <p class="copyright">(C) 2016-2019 {{ $t('Footer.copyright_holder') }}</p>
    </footer>
  </div>
</template>


<style lang="scss" scoped>
  @import 'includes/_variables';

  $_width: $dimen-content-width;

  .Footer {
    width: 100%;
    background-color: $color-background-white;
    box-shadow: 0px 0px 3px 1px $color-shadow-white;
    line-height: 1.55;

    &, * {
      box-sizing: border-box;
    }

    footer {
      display: flex;
      flex-direction: row;
      margin: 0 auto;
      padding: 30px 15px 25px;
      width: $_width;

      /**
       * Menus
       */
      .menus {
        margin: 0 20px 0 0;
        padding: 0;
        flex: 1 1 auto;
        align-self: flex-end;

        color: $color-gray;
        text-align: right;
        font-size: $font-xsmall;

        li {
          display: inline-block;
          margin: 0;
          list-style-position: inside;
          list-style-type: none;

          &::before {
            display: inline;
            margin: 0 6px 0 4px;
            content: '|';
          }

          &:first-child {
            &::before {
              display: none;
            }
          }
        }
      }

      /**
       * Copyright
       */
      .copyright {
        margin: 0 0 0;
        align-self: flex-end;
        letter-spacing: .8px;
        font-size: $font-xsmall;
        color: $color-gray;
      }
    }
  }

</style>


<script>
  import SweetScroll from 'sweet-scroll'

  export default {
    methods: {
      scroll() {
        const scroller = new SweetScroll({ easing: 'easeOutQuad' })
        scroller.toTop(0)
      },
    },
  }
</script>
