<template>
  <div class="RecentlyLog">
    <div class="carousel" ref="carousel">
      recently
    </div>
  </div>
</template>


<style lang="scss" scoped>
  @import 'includes/_variables';
  @import 'includes/_mixins';
</style>


<script>
  import 'flickity/css/flickity.css'
  import Flickity from 'flickity'

  export default {
    data: () => ({
      flkty: null,
      records: [],
    }),
    mounted() {
      this.$nextTick(() => {
        this.flkty = new Flickity(
          this.$refs.carousel,
          {
            contain: true,
            setGallerySize: false,
            wrapAround: true,
          })
      })
    }
  }
</script>
