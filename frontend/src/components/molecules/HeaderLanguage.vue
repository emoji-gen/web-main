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

  import { setLocale, toLocalizedPath, toUnlocalizedPath } from '@/src/locales'
  import eventbus from '@/src/eventbus'
  import { LOCALE } from '@/src/initial_state'

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

  const INITIAL_LANGUAGE =
    LANGUGAGES.find(v => v.key === LOCALE) || LANGUGAGES[0]

  export default {
    data: () => ({
      selected: INITIAL_LANGUAGE,
      options: LANGUGAGES,
    }),
    methods: {
      changed() {
        if (!this.selected) {
          log.info('Locale not selected.')
          return
        }

        const locale = this.selected.key
        setLocale(locale)
        this.$i18n.locale = locale
        eventbus.$emit('EG_LOCALE_CHANGED', locale)

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
