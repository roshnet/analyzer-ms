<template>
  <card-base>
     <apex-chart
      :series="series"
      :options="options"
      type="scatter"
      height="300px"
      width="300px"
    />
  </card-base>
</template>

<script>
export default {
  components: {
    CardBase: () => import(/* webpackChunkName: "CardBaseComponent" */'components/CardBase'),
    ApexChart: () => import(/* webpackChunkName: "ApexChartRoot" */'vue-apexcharts')
  },

  props: {
    series: {
      required: true
    },
    options: {
      required: false,
      default: {
        xaxis: {
          // categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
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
