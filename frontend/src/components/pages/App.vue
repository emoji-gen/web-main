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
      eventbus.$on('CE_SEARCH_JOINED_TEAMS', () => {
        this.$ptero.emit('CE_SEARCH_JOINED_TEAMS')
      })
    },
  }
</script>
