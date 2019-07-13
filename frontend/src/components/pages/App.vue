<template>
  <div class="App">
    <Background/>
    <Header/>
    <div class="body">
      <router-view/>
    </div>
    <Footer/>
  </div>
</template>


<style lang="scss" scoped>
  .App {
    position: relative;

    .body {
      margin-bottom: 180px;
      min-height: 600px;
    }
  }
</style>


<script>
  import log from 'loglevel'

  import eventbus from '@/src/eventbus'
  import { getLocale, setLocale } from '@/src/locales'


  export default {
    created() {
      this.$ptero.on('CE_ATTACH', e => {
        log.debug('Attached by Chrome Extension', e.detail)
      })

      eventbus.$on('EG_LOCALE_CHANGE', locale => {
        if (getLocale() !== locale) {
          setLocale(locale)
          this.$i18n.locale = locale
          eventbus.$emit('EG_LOCALE_CHANGED', locale)
        }
      })
    },
  }
</script>
