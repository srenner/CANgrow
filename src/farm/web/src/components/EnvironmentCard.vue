<script setup lang="ts">
    const props = defineProps(['env'])
</script>

<template>
    <div className="w-full bg-white rounded-lg shadow-lg overflow-hidden flex items-center p-6">
        <div className="w-32 h-32 bg-gray-300 flex items-center justify-center flex-shrink-0 rounded">
          <svg className="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 21h18M5 21V11l7-6 7 6v10M12 5v16M5 11h14M7 14h10M7 17h10" />
          </svg>
        </div>
        
        <div className="pl-6 flex-1">
          <h2 className="text-2xl font-bold text-gray-800 mb-2">{{ env.name }}</h2>
          <p className="text-gray-600 mb-4">
            {{ env.descr }}
          </p>
          
          <div className="flex items-center justify-between">
            <span className="text-sm text-gray-500">more stats</span>
            <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition">
              Details
            </button>
          </div>
        </div>
      </div>
</template>

<style scoped>
</style>
