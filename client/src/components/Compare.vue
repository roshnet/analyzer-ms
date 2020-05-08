<template>
  <main>
    <div class="text-h6 text-weight-light">
      Pick one column out of
      <q-btn-dropdown
        :disable="!columnsReady"
        :loading="!columnsReady"
        dense
        class="bg-transparent text-green"
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

    <div>
      <Graph
        v-for="(graph, i) in graphsPayload"
        :key="i"
        :series="graph.series"
        :options="graph.options"
      />
    </div>
  </main>
</template>

<script>
export default {
  components: {
    Graph: () => import(/* webpackChunkName: "GraphComponent" */'components/Graph')
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

      // everything the Graph component needs
      graphData: null,

      // a list of objects as payload for the Graph component
      graphsPayload: null
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
      /*
      Every click on dropdown menu results in another API call.
      This needs to be avoided.
      A better strategy will be to call the API on mount, and store all
      content in a Vuex store. The other functions will then simply remodel
      the stored data, and provide that to the Graph component via a cached
      property.
      */
      this.activecolumn = column      
      const endpoint = process.env.DEV_API + '/pivot?about=' + column
      this.$axios
        .get(endpoint)
        .then((response) => {
          this.graphData = response.data.result
        })
        .catch((err) => {
          console.error(">>> Shit hit the fan: ", err)
        })
    }
  },

  watch: {
    graphData() {
      let _graphs = []
      for (let block of this.graphData['y_axis']) {
        _graphs.push({
          series:[{
            name: block['column'],
            data: block['values']
          }],
          options: {
            yaxis: {
              title: {
                text: block['column']
              }
            },
            xaxis: {
              title: {
                text: this.activecolumn
              }
            }
          }
        })
      }
      this.graphsPayload = _graphs
    },
  },

  mounted() {
    this.getColumnNames()
  }
}
</script>
