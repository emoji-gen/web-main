<template>
  <div class="ColorKind">
    <ul>
      <li>
        <input type="radio"
          name="ColorKind__kind"
          value="foreground"
          id="ColorKind__kind--foreground"
          v-model="kind">
        <label for="ColorKind__kind--foreground"
          v-t="'ColorKind.foreground_label'" />
      </li>
      <li>
        <input type="radio"
          name="ColorKind__kind"
          value="background"
          id="ColorKind__kind--background"
          v-model="kind">
        <label for="ColorKind__kind--background"
          v-t="'ColorKind.background_label'" />
      </li>
    </ul>
  </div>
</template>
