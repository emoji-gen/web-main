<template>
  <div class="Home">
    <Generator />
  </div>
</template>


<style lang="scss">
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
