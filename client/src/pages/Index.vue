<template>
  <q-page class="flex flex-center">
    <div>
      hi
      <chart :series="series" :options="chartOptions" type="line"></chart>
    </div>
  </q-page>
</template>

<script>
import VueApexChart from 'vue-apexcharts'

export default {
  name: 'PageIndex',

  components: {
    Chart: VueApexChart
  },

  data() {
    return {
      series: [{
        name: 'Top Score',
        data: [50, 40, 45, 50, 49, 60, 70, 19]
      }],
      chartOptions: {
        chart: {
          type: 'line',
          height: 'auto',
          zoom: {
            enabled: false
          }
        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998]
        },
        grid: {
          row: {
            borderColor: ['#f00', '#00f'],
            opacity: 0.8,
            show: true,
            strokeDashArray: 0,
            xaxis: {
              lines: {
                show: true
              }
            }
          }
        }
      }
    }
  }
}
</script>
