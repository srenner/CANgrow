<script setup lang="ts">
  import router from '@/router';
  import { useRouter } from 'vue-router';

  useRouter();
  const props = defineProps(['env']);
  const id = props.env.id.toString();

  const goToEnvironment = () => {
    router.push('/environment/' + id);
  }
</script>

<template>
  <div class="w-full bg-white dark:bg-gray-800 rounded-lg shadow-lg overflow-hidden flex items-center p-6">
    <div class="w-32 h-32 bg-gray-300 dark:bg-gray-700 flex items-center justify-center flex-shrink-0 rounded">
      <img src="../assets/ai/placeholder-greenhouse.svg" />
    </div>

    <div class="pl-6 flex-1">
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-100 mb-2">{{ env.name }}</h2>
      <p class="text-gray-600 dark:text-gray-300 mb-4">
        {{ env.descr }}
      </p>
    </div>
    <div class="flex items-center justify-between">
      <button @click="goToEnvironment" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition">
        Details
      </button>
    </div>
  </div>
</template>

<style scoped>
</style>
