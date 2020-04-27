<template>
  <div
    class="q-my-lg q-py-xs text-center"
    :style="'backgroundColor: ' + bg + '; color: ' + font"
  >
    <slot>Get Started!</slot>
  </div>
</template>

<script>
export default {
  props: {
    bg: {
      default: '#006'
    },
    font: {
      default: '#999'
    }
  }
}
</script>
