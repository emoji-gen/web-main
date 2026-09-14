<template>
  <div class="DocumentTitle">
  </div>
</template>


<script>
  export default {
    props: {
      value: String,
    },
    watch: {
      value(value) {
        document.title = value
      },
    },
    mounted() {
      document.title = this.value
    },
  }
</script>
