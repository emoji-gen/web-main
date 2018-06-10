<template>
  <div class=eg-app>Hello</div>
</template>

<script>
export default {
  created() {
    this.$ptero.on('CE_ATTACH', e => {
      if (meta.env.debug) {
        console.log('attached by Chrome Extension', e.detail)
      }
      this.$broadcast('CE_ATTACH', e.detail)
    })
    this.$ptero.on('CE_SEARCH_JOINED_TEAMS_DONE', e => {
      if (meta.env.debug) { console.log('CE_SEARCH_JOINED_TEAMS_DONE', e.detail) }
      this.$broadcast('CE_SEARCH_JOINED_TEAMS_DONE', e.detail)
    })
    this.$ptero.on('CE_REGISTER_EMOJI_DONE', e => {
      if (meta.env.debug) { console.log('CE_REGISTER_EMOJI_DONE', e.detail) }
      this.$broadcast('CE_REGISTER_EMOJI_DONE', e.detail)
    })
  },
}
</script>

<style lang="scss" scoped>

.eg-app {
  position: relative;
  margin: 0;
  padding: 0;
}

</style>
