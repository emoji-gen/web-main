<template>
  <div class="Contact">Contact</div>
</template>


<style lang="scss">
  .Contact {

  }
</style>


<script>
  export default {
    mounted() {
      this.$store.dispatch('contact/mounted')
    }
  }
</script>
