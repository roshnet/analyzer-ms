<template>
  <card-base>
     <apex-chart height="300px" width="300px" type="scatter" :options="chartOptions" :series="series" />
  </card-base>
</template>

<script>
export default {
  components: {
    CardBase: () => import(/* webpackChunkName: "CardBaseComponent" */'components/CardBase'),
    ApexChart: () => import(/* webpackChunkName: "ApexChartRoot" */'vue-apexcharts')
  },

  data() {
    return {
      series: [{
        name: 'Item',
        data: [3,4,6,7,4,2,5,7,8,]
      }],
      chartOptions: {
        xaxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
          labels: {
            style: {
              colors: '#fff'
            }
          }
        }
      }
    }
  }
}
</script>
