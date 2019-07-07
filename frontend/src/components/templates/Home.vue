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
  import { HOME_TITLE } from '@/src/initial_state'

  export default {
    mounted() {
      document.title = HOME_TITLE
    },
  }
</script>
