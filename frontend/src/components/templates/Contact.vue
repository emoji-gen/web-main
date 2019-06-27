<template>
  <div class="Contact">Contact</div>
</template>


<style lang="scss" scoped>
  .Contact {

  }
</style>


<script>
  const TITLE = window.CONTACT_TITLE || ''

  export default {
    mounted() {
      document.title = TITLE
    }
  }
</script>
