<template>
  <q-page class="flex flex-center">
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
      fetchedContent: [],
      series: [],
      chartOptions: {
        xaxis: {
           categories: []
        }
      }
    }
  }
}
</script>
