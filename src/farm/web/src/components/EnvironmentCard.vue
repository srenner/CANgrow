<script setup lang="ts">
    const props = defineProps(['env'])
</script>

<template>
  <div className="w-full bg-white rounded-lg shadow-lg overflow-hidden flex items-center p-6">
    <div className="w-32 h-32 bg-gray-300 flex items-center justify-center flex-shrink-0 rounded">
      <img src="../assets/ai/placeholder-greenhouse.svg" />
    </div>

    <div className="pl-6 flex-1">
      <h2 className="text-2xl font-bold text-gray-800 mb-2">{{ env.name }}</h2>
      <p className="text-gray-600 mb-4">
        {{ env.descr }}
      </p>
    </div>
    <div className="flex items-center justify-between">
      <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition">
        Details
      </button>
    </div>
  </div>
</template>

<style scoped>
</style>
