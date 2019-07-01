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
  import { HOME_TITLE } from '@/src/initial_state'

  export default {
    mounted() {
      document.title = HOME_TITLE
    },
  }
</script>
