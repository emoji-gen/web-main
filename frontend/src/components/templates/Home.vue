<template>
  <div class="Home">
    <Result />
    <Generator />
    <RecentlyLog />
  </div>
</template>


<style lang="scss" scoped>
  .Home {
  }
</style>


<script>
  export default {
    mounted() {
      document.title = this.$t('Home.title')
    },
  }
</script>
