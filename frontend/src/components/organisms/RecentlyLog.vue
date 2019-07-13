<template>
  <div class="RecentlyLog">
    <h2 v-t="'RecentlyLog.title'"></h2>
    <div class="carousel" ref="carousel">
    </div>
  </div>
</template>


<style lang="scss">
  @import 'includes/_variables';
  @import 'includes/_mixins';

  .RecentlyLog {
    @extend %box;
    padding: 32px 32px (32px + 28px) 32px;
    line-height: 1.55;

    &, * {
      box-sizing: border-box;
    }
    h2 {
      @extend %box-heading;
    }

    .carousel {
      $_border-width: 1px;
      height: ($dimen-emoji-size + $_border-width * 2);

      .carousel-cell {
        box-sizing: content-box;
        width: $dimen-emoji-size;
        height: $dimen-emoji-size;
        margin-right: 10px;
        border: $_border-width solid rgba(0, 0, 0, 0.18);
        border-radius: 5px;
        background-repeat: no-repeat;
        background-position: center center;
      }
    }
  }
</style>


<script>
  import 'flickity/css/flickity.css'
  import Flickity from 'flickity'

  import eventbus from '@/src/eventbus'
  import { LOCALE, RECENTLY_LOGS } from '@/src/initial_state'
  import { getLocale } from '@/src/locales'

  export default {
    data: () => ({
      flkty: null,
      recentlyLogs: RECENTLY_LOGS[LOCALE],
    }),

    created() {
      eventbus.$on('EG_LOCALE_CHANGED', () => {
        this.recentlyLogs = RECENTLY_LOGS[getLocale()]
        this.redraw()
      })
    },
    mounted() {
      this.$nextTick(() => {
        this.flkty = new Flickity(
          this.$refs.carousel,
          {
            contain: true,
            setGallerySize: false,
            wrapAround: true,
          })

        this.redraw()
      })
    },

    methods: {
      redraw() {
        this.flkty.remove(this.flkty.getCellElements())

        const baseNode = document.createElement('div')
        baseNode.className = 'carousel-cell'

        for (const recentlyLog of this.recentlyLogs) {
          const node = baseNode.cloneNode(true)
          node.style.backgroundImage = `url('${recentlyLog.url}')`
          node.title = recentlyLog.text.replace(/\n/g, '')
          this.flkty.append(node)
        }
      },
    },
  }
</script>
