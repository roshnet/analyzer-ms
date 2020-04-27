<template>
  <q-card class="fit" :style="{backgroundColor: bgColor}"  >
    <q-card-section>
      <slot></slot>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: 'CardBase',
  props: {
    bgColor: {
      default: '#2B2D3E5'
    }
  }
}
</script>
