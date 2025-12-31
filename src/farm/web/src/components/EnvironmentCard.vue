<script setup lang="ts">
    const props = defineProps(['env'])
</script>

<template>
    <div className="w-full bg-white rounded-lg shadow-lg overflow-hidden flex items-center p-6">
        <div className="w-32 h-32 bg-gray-300 flex items-center justify-center flex-shrink-0 rounded">
          <svg className="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
          </svg>
        </div>
        
        <div className="pl-6 flex-1">
          <h2 className="text-2xl font-bold text-gray-800 mb-2">{{ env.name }}</h2>
          <p className="text-gray-600 mb-4">
            {{ env.descr || 'of all the environments, this is one of them' }}
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
