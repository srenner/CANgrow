<script setup lang="ts">
    const props = defineProps(['env'])
</script>

<template>
    <div>
        {{env.name}}
    </div>
</template>

<style scoped></style>