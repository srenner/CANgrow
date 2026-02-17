<script setup lang="ts">
  import { onMounted } from 'vue'
  import Header from './components/Header.vue';

  onMounted(() => {
    //
  });

</script>

<template>
  <div class="min-h-screen bg-white text-gray-900 dark:bg-gray-950 dark:text-gray-100 transition-colors duration-300">
    <Header />
    <RouterView />
  </div>
</template>

<style scoped></style>
