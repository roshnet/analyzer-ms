<template>
  <div>
    <q-btn-dropdown :disable="!columnsReady" color="primary" label="Available Columns">
      <q-list>
        <q-item
          v-for="(column, i) in columns"
          :key="i"
          @click="getPivotValues(column)"
          clickable
          v-close-popup
        >
          <q-item-section>
            <q-item-label>{{ column }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // hold names of all columns as an array
      columns: [],

      // do not activate the dropdown until the columns are done fetching
      columnsReady: false,
    }
  },

  methods: {
    getColumnNames() {
      const endpoint = process.env.DEV_API + '/summary'
      this.$axios
        .get(endpoint)
        .then((response) => {
          this.columns = Object.keys(response.data.result)
          this.columnsReady = true  // enables the columns dropdown
        })
        .catch((err) => {
          console.error(">>> Shit hit the fan: ", err)
        })
    },

    getPivotValues(column) {
      const endpoint = process.env.DEV_API + '/pivot?about=' + column
      this.$axios
        .get(endpoint)
        .then((response) => {
          console.warn(response.data.result);
        })
        .catch((err) => {
          console.error(">>> Shit hit the fan: ", err)
        })
    }
  },

  beforeMount() {
    this.getColumnNames()
  }
}
</script>
