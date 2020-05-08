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
      type: Array,
      required: true
    },
    options: {
      required: false,
      type: Object,
      default: function () {
        return {
          xaxis: {
            labels: {
              style: {
                colors: '#0f0'
              }
            }
          },
          chart: {
            foreColor: '#0f0',
            background: '#000'
          },
          title: {
            text: 'Some Samples',
            align: 'left',
            style: {
              color: '#0a0'
            }
          },
          theme: {
            mode: 'dark',
            palette: 'palette1'
          }
        }
      }
    }
  }
}
</script>
