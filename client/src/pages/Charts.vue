<template>
  <q-page class="flex flex-center">
    <div>
      charts
      <chart :series="series" :options="chartOptions" height="400" width="500"></chart>
    </div>
  </q-page>
</template>

<script>
import VueApexChart from 'vue-apexcharts'

export default {
  name: 'PageCharts',
  
  components: {
    Chart: VueApexChart
  },

  data() {
    return {
      series: [
        {
          // the info for the second plot
          name: "Smartphones",
          data: [23, 34, 45, 56, 67, 78]
        },
        {
          // the info for the first plot
          name: "Televisions",
          data: [28, 29, 33, 36, 32, 32, 33]
        },
      ],
      chartOptions: {
        chart: {
          type: 'bar',
          height: 400
        },
        colors: ['#080', '#008'],
        xaxis: {
           categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        }
      }
    }
  }
}
</script>