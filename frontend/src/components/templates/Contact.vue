<template>
  <div class="Contact">Contact</div>
</template>


<style lang="scss">
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
