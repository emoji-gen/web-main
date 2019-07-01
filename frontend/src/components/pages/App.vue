<template>
  <div class="App">
    <Background/>
    <Header/>
    <router-view/>
    <Footer/>
  </div>
</template>


<style lang="scss" scoped>
  .App {
    position: relative;
  }
</style>


<script>
  import log from 'loglevel'
  import eventbus from '@/src/eventbus'

  export default {
    created() {
      this.$ptero.on('CE_ATTACH', e => {
        log.debug('Attached by Chrome Extension', e.detail)
        eventbus.$emit('CE_ATTACH', e.detail)
      })
      this.$ptero.on('CE_SEARCH_JOINED_TEAMS_DONE', e => {
        log.debug('CE_SEARCH_JOINED_TEAMS_DONE', e.detail)
        eventbus.$emit('CE_SEARCH_JOINED_TEAMS_DONE', e.detail)
      })
      this.$ptero.on('CE_REGISTER_EMOJI_DONE', e => {
        log.debug('CE_REGISTER_EMOJI_DONE', e.detail)
        eventbus.$emit('CE_REGISTER_EMOJI_DONE', e.detail)
      })
    },
  }
</script>
