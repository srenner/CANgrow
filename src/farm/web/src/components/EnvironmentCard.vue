<script setup lang="ts">
    const props = defineProps(['env'])
</script>

<template>
    <div class="env-card">
        {{env.name}}
    </div>
</template>

<style scoped>
    .env-card {
        border: solid 1px black;

    }

</style>