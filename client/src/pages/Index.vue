<template>
  <q-page class="flex flex-center">
    <div class="q-mx-lg">
      <p class="text-subtitle1 text-center">
        To get started, upload an Excel spreadsheet file.
      </p>
      <p class="text-center">
        <!-- <q-btn
          glossy
          icon-right="file_upload"
          label="Upload"
          class="q-ma-lg"
        /> -->
        <q-uploader
          url="http://localhost:4444/upload"
          dark
          color="green"
        />
      </p>
    </div>
  </q-page>
</template>
