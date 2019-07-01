<template>
  <div class="Home">
    <Result />
    <Generator />
    <RecentlyLog />
  </div>
</template>


<style lang="scss" scoped>
  .Home {
    margin-bottom: 180px;
    min-height: 600px;
  }
</style>


<script>
  const TITLE = window.HOME_TITLE || ''

  export default {
    mounted() {
      document.title = TITLE
    }
  }
</script>
