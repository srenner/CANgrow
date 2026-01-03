<script setup lang="ts">
    import { useRoute } from 'vue-router';
    import { ref, onMounted, computed } from 'vue'
    import type { EnvironmentPublic } from '@/api/types.gen';
    import { Environment as EnvironmentService } from '@/api/sdk.gen';

    const route = useRoute()
    const id = computed(() => parseInt(route.params.id as string))

    const environment = ref<EnvironmentPublic>();
    const loading = ref(false);
    const error = ref<string | null>(null);

    onMounted(() => {
        loadEnvironment();
    });

    async function loadEnvironment() {
        loading.value = true;
        error.value = null;
        try {
            const { data } = await EnvironmentService.getEnvironment({ path: { id: id.value } });            
            environment.value = data
        }
        catch(err: any) {
            error.value = err.message || 'Error loading environment ' + id

        }
        finally {
            loading.value = false;
        }
    }

</script>

<template>
    
        <h1>{{ environment?.name }}</h1>
        <div>
            <div v-if="loading">Loading...</div>
            <div v-else-if="error">{{ error }}</div>
            <div v-else>
                {{ environment }}
            </div>
        </div>
    
</template>

<style scoped></style>