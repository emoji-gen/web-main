<template>
  <div class="ColorKind">
    <ul>
      <li>
        <input type="radio"
          name="ColorKind__kind"
          value="foreground"
          id="ColorKind__kind--foreground"
          v-model="colorKind">
        <label for="ColorKind__kind--foreground"
          v-t="'ColorKind.foreground_label'" />
      </li>
      <li>
        <input type="radio"
          name="ColorKind__kind"
          value="background"
          id="ColorKind__kind--background"
          v-model="colorKind">
        <label for="ColorKind__kind--background"
          v-t="'ColorKind.background_label'" />
      </li>
    </ul>
  </div>
</template>


<style lang="scss" scoped>
  @import 'includes/_variables';

  .ColorKind {
    $_border-radius: 6px;

    ul {
      display: flex;
      justify-content: flex-end;
      list-style-type: none;
      list-style-position: inside;
      margin: 0;

      li {
        display: block;

        &:first-of-type {
          input:checked + label {
            border-right-width: 1px;
          }

          label {
            border-right-width: 0;
            border-radius: $_border-radius 0 0 $_border-radius;
          }
        }

        &:last-of-type {
          input:checked + label {
            border-left-width: 1px;
          }

          label {
            border-left-width: 0;
            border-radius: 0 $_border-radius $_border-radius 0;
          }
        }

        label {
          display: block;
          padding: 2.7px 10px;
          border: 1px solid rgba(0, 0, 0, .18);
          color: rgba(0, 0, 0, .32);
          font-size: $font-small;
          cursor: pointer;
        }

        input {
          display: none;

          &:checked + label {
              border: 1px solid rgba(darken($color-blue, 20%), .8);
              color: darken($color-blue, 20%);
          }
        }
      }
    }
  }

</style>


<script>
  export default {
    data: () => ({
      colorKind: 'foreground',
    }),
    watch: {
      colorKind(value) {
        this.$emit('change', value)
      },
    },
  }
</script>
