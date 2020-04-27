<template>
  <q-layout view="lHh Lpr lFf">
    <main class="non-selectable">
      <!-- The primary block -->
      <div class="q-pa-lg">
        <p class="q-py-xl text-h2 text-weight-medium">
          Visual insights from your data
        </p>
        <p class="text-h4">
          Say hello to data analytics.
        </p>
      </div>

      <!-- Subsequent blocks -->
      <block>
        <h4>Get started!</h4>
      </block>
    </main>
  </q-layout>
</template>

<script>
import Block from 'components/landing/Block'

export default {
  name: 'HomeLayout',

  components: {
    Block
  }
}
</script>

<style scoped>
main div {
  background-color: #008;
  color: #fff;
}
</style>
