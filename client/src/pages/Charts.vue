<template>
  <q-page class="q-ma-lg">
    <div class="row q-col-gutter-md">
      <div class="col-12 q-pa-md">
        <q-markup-table>
          <thead>
            <tr>
               <th
                 v-for="(column, idx) in columnNames"
                 class="text-center"
                 :key="idx"
                >
                  {{ column }}
                </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(row, i) in rows" :key="i">
              <td v-for="(item, ii) in row" class="text-center" :key="ii">
                {{ item }}
              </td>
            </tr>
          </tbody>
        </q-markup-table>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'ChartsPage',

  data() {
    return {
      totalData: null,
      columnNames: null,
      rows: []
    }
  },

  methods: {
    fetchColumnData() {
      const endpoint = process.env.DEV_API + '/summary'
      // The axios call executes in a different routine by itself,
      // i.e. it is non-blocking in nature by default.
      this.$axios
        .get(endpoint)
        .then((response) => {
          this.totalData = response.data.result
          this.columnNames =  Object.keys(this.totalData)
          this.fillRows()          
        })
        .catch((err) => {
          console.error(">>> Shit hit the fan: ", err)
        })
    },
    fillRows() {
      /*
      This logic was written by me (@roshnet) when I hadn't slept for over 30
      hours. Please be kind to file a GitHub issue about anything you think
      seems off.
      */

      // #-of-items per row ('0' here can be anything, since all fields are
      // assumed to have the same number of items)
      let arbitraryRow = this.totalData[this.columnNames[0]];

      for (let r in arbitraryRow) {
        let row = Array()
        for (let col of this.columnNames) {
          row.push(this.totalData[col][r])
        }
        this.rows.push(row)
      }
    }
  },

  mounted() {
    this.fetchColumnData()
  }
}
</script>
