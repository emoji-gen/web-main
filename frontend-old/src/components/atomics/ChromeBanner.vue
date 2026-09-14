<template>
  <div class="ChromeBanner">
    <a :href="storeUrl" target="_blank" rel="noopener">
      <img
        src="/assets/img/chrome_web_store-248x75@1x.png"
        srcset="/assets/img/chrome_web_store-248x75@1x.png 1x, /assets/img/chrome_web_store-248x75@2x.png 2x"
        width="248" height="75"
        alt="available in the chrome web store"
        decoding="async" loading="lazy">
    </a>
  </div>
</template>


<script>
  import eventbus from '@/src/eventbus'
  import { getLocale } from '@/src/locales'

  const INITIAL_LOCALE = getLocale()
  const STORE_URL = 'https://chrome.google.com/webstore/detail/ghbhakkknnmocmiilhneahbkiaegdnmf'

  // ------------------------------------------------------

  export default {
    data: () => ({
      storeUrl: STORE_URL + '?hl=' + INITIAL_LOCALE,
    }),

    created() {
      eventbus.$on('EG_LOCALE_CHANGED', locale => {
        this.storeUrl = STORE_URL + '?hl=' + locale
      })
    },
  }
</script>
