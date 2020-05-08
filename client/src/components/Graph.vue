<template>
  <card-base>
     <apex-chart
      :series="series"
      :options="options"
      type="scatter"
      height="280px"
      width="250px"
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
      required: true,
      type: Object
    }
  },

  computed: {
    defaultOptions() {
      return {
        // some valid JSON
        xaxis: {
          title: {
            style: {
              color: '#f00',
              fontSize: '12px',
            }
          },
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
        theme: {
          mode: 'dark',
          palette: 'palette1'
        }
      }
    }
  },

  mounted() {
    // Merge `this.defaultOptions` in the `options` attribute of incoming
    // `options` object
    //this.options = {...this.options, ...this.defaultOptions}  // partially works

  }
}
</script>
