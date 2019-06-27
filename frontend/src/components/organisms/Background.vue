<template>
  <div class="Background">
    <div class="blue"></div>
    <div class="red"></div>
    <div class="green"></div>
    <div class="yellow"></div>
  </div>
</template>


<style lang="scss">
  @import 'includes/_variables';

  $_opacity: 0.4;
  $_height: 1900px;
  $_rotate: -18deg;

  .Background {
    position: fixed;
    top: 0;
    right: 0;
    left: 0;
    box-sizing: border-box;
    height: $_height;
    overflow: hidden;
    z-index: -1;

    .blue {
      position: absolute;
      top: 100px;
      left: -30px;
      width: 800px;
      height: 10px;
      background-color: $color-blue;
      opacity: $_opacity;
      transform: rotate($_rotate);
    }

    .red {
      position: absolute;
      top: 170px;
      left: -50px;
      width: 1250px;
      height: 10px;
      background-color: $color-red;
      opacity: $_opacity;
      transform: rotate($_rotate);
    }

    .green {
      position: absolute;
      top: -100px;
      left: 320px;
      width: 10px;
      height: 2100px;
      background-color: $color-green;
      opacity: $_opacity;
      transform: rotate($_rotate);
    }

    .yellow {
      position: absolute;
      top: -100px;
      left: 450px;
      width: 10px;
      height: 2100px;
      background-color: $color-yellow;
      opacity: $_opacity;
      transform: rotate($_rotate);
    }
  }

</style>
