<template>
  <div class="HeaderLaungage">
    <multiselect
      label="label"
      track-by="key"
      :allow-empty="false"
      :options="options"
      :show-labels="false"
      placeholder=""
      v-model="selected"
      @input="changed"
    />
  </div>
</template>


<style lang="scss">
  @import 'includes/_variables';
  @import 'includes/_mixins';

  $_height: 74px;

  .HeaderLaungage {
    .multiselect {
      width: 180px;
      color: $color-gray;
    }
    .multiselect__single,
    .multiselect__option,
    .multiselect__input {
      line-height: 1.55;
      font-size: $font-medium;
    }
  }
</style>


<script>
  import log from 'loglevel'
  import VueMultiselect from 'vue-multiselect/src/Multiselect.vue'

  import {
    getLocale,
    setLocale,
    toLocalizedPath,
    toUnlocalizedPath,
  } from '@/src/locales'

  import eventbus from '@/src/eventbus'

  // ------------------------------------------------------

  const LANGUGAGES = [
    {
      key: 'ja',
      label: '日本語',
    },
    {
      key: 'ko',
      label: '한국어',
    },
    {
      key: 'en',
      label: 'English',
    },
  ]

  const INITIAL_LOCALE = getLocale()
  const INITIAL_LANGUAGE =
    LANGUGAGES.find(v => v.key === INITIAL_LOCALE) || LANGUGAGES[0]

  // ------------------------------------------------------

  export default {
    data: () => ({
      selected: INITIAL_LANGUAGE,
      options: LANGUGAGES,
    }),

    created() {
      eventbus.$on('EG_LOCALE_CHANGED', locale => {
        this.selected = LANGUGAGES.find(v => v.key === locale)
      })
    },
    methods: {
      changed() {
        if (!this.selected) {
          log.info('Locale not selected.')
          return
        }

        const locale = this.selected.key
        const path = toLocalizedPath(toUnlocalizedPath(this.$route.path), locale)
        const { query } = this.$route
        this.$router.push({ path, query })
      },
    },
    components: {
      multiselect: VueMultiselect,
    },
  }
</script>
