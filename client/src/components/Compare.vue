<template>
  <div>
    <div class="text-h6 text-weight-light">
      Pick one column out of
      <q-btn-dropdown
        :disable="!columnsReady"
        class="bg-transparent text-green"
        dense
        :loading="!columnsReady"
        label="Available Columns"
      >
        <q-list>
          <q-item
            v-for="(column, i) in columns"
            :key="i"
            @click="getPivotValues(column); showAnalyzerHeader=true"
            clickable
            v-close-popup
          >
            <q-item-section>
              <q-item-label>{{ column }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-btn-dropdown>
      to analyze
    </div>

    <!-- The multi-graph section -->
    <div v-if="showAnalyzerHeader" class="q-my-md q-pa-sm bg-dark">
      <h3 class="text-weight-light q-pa-sm text-overline" style="font-size: 150%;">
        Analyzing column <code class="bg-green-9 q-pa-xs">{{ activecolumn }}</code>
      </h3>
    </div>
  </div>
</template>

<script>
export default {
  components: {
    // Graph: () => import(/*webpackChunkName: Graph*/'components/Graph')
  },

  data() {
    return {
      // hold names of all columns as an array
      columns: [],

      // do not activate the dropdown until the columns are done fetching
      columnsReady: false,

      // show analyzer section heading only when a value is selected
      showAnalyzerHeader: false,

      // the column to pivot against (aka the active column)
      activecolumn: null,
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
      this.activecolumn = column
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
