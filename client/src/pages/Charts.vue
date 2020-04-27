<template>
  <q-page class="flex flex-center">
    {{ columns }}
    <div class="row q-col-gutter-md">
      <div class="col-md-6 col-sm-12 col-xs-12">
        <graph></graph>
      </div>
      <div class="col-md-6 col-sm-12 col-xs-12">
        <graph></graph> 
      </div>
      <div class="col-md-6 col-sm-12 col-xs-12">
        <graph></graph>
      </div>
      <div class="col-md-6 col-sm-12 col-xs-12">
        <graph bgColor="red"></graph>
      </div>
      <div class="col-md-6 col-sm-12 col-xs-12">
        <graph></graph>
      </div>
      <div class="col-md-6 col-sm-12 col-xs-12">
        <graph></graph>
      </div>
    </div>
  </q-page>
</template>

<script>
import Graph from 'components/Graph'

export default {
  name: 'ChartsPage',

  components: {
    Graph
  },

  data() {
    return {
      columns: [],
      series: [],
      chartOptions: {
        xaxis: {
           categories: []
        }
      }
    }
  },

  methods: {
    fetchColumnNames() {
      const endpoint = process.env.API + 'view-columns'
      // The axios call executes in a different routine by itself,
      // i.e. it is non-blocking in nature by default.
      this.$axios
        .get(endpoint)
        .then((response) => {
          this.columns = response.data.result
        })
    }
  },

  created() {
    this.fetchColumnNames()
  }
}
</script>
