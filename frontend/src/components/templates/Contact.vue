<template>
  <div class="Contact">Contact</div>
</template>


<style lang="scss" scoped>
  .Contact {
  }
</style>


<script>
  import { CONTACT_TITLE } from '@/src/initial_state'

  export default {
    mounted() {
      document.title = CONTACT_TITLE
    },
  }
</script>
