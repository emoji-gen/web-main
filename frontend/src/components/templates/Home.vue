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
  export default {
    mounted() {
      this.$store.dispatch('home/mounted')
    }
  }
</script>
