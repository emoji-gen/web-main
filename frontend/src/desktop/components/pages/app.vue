<template>
  <div class="v-cloak" :class="$style.App">
    <Header></Header>
  </div>
</template>


<script>

import Header from 'desktop/components/organisms/header.vue'

export default {
  created() {
    this.$ptero.on('CE_ATTACH', e => {
      if (DEBUG) {
        console.log('Attached by Chrome Extension', e.detail)
      }
      this.$store.dispatch('attachExtension')
    })
    this.$ptero.on('CE_SEARCH_JOINED_TEAMS_DONE', e => {
      if (DEBUG) {
        console.log('CE_SEARCH_JOINED_TEAMS_DONE', e.detail)
      }
      //this.$broadcast('CE_SEARCH_JOINED_TEAMS_DONE', e.detail)
    })
    this.$ptero.on('CE_REGISTER_EMOJI_DONE', e => {
      if (DEBUG) {
        console.log('CE_REGISTER_EMOJI_DONE', e.detail)
      }
      //this.$broadcast('CE_REGISTER_EMOJI_DONE', e.detail)
    })
  },

  components: {
    Header,
  },
}
</script>


<style lang="scss" module>

  .App {
    position: relative;
    margin: 0;
    padding: 0;
  }

</style>
