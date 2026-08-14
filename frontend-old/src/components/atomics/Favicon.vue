<template>
  <div class="Favicon">
  </div>
</template>


<script>
  import log from 'loglevel'
  import eventbus from '@/src/eventbus'

  export default {
    created() {
      eventbus.$on('EG_LOCALE_CHANGED', locale => {
        const elem = document.querySelector('link[rel="icon"]')
        if (!elem) {
          log.error('A link element for favicon not found')
          return
        }

        const faviconUrl = `/assets/img/favicon_${locale}.ico`
        elem.href = faviconUrl
      })
    },
  }
</script>
