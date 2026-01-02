<script setup lang="ts">
    import { ref, onMounted } from 'vue'
    import type { Environment } from '@/api/types.gen';
    import { Environment as EnvironmentService } from '@/api/sdk.gen';
    import EnvironmentCard from '@/components/EnvironmentCard.vue';

    const environments = ref<Environment[]>([]);
    const loading = ref(false);
    const error = ref<string | null>(null);

    onMounted(() => {
        loadEnvironments();
    });

    async function loadEnvironments() {
        loading.value = true;
        error.value = null;
        try {
            const response = await EnvironmentService.listEnvironments();
            if(response.data) {
                environments.value = response.data;
            }
            else {
                console.log(response);
            }
        }
        catch {

        }
        finally {
            loading.value = false;
        }
    }

</script>

<template>
    <h1>Environments</h1>
    <div>
        
        <div v-if="loading">Loading...</div>
        <div v-else-if="error">{{ error }}</div>
        <div v-else class="gap-4">
            <div v-for="env in environments" :key="env.id!" class="mb-4">
                <EnvironmentCard :env="env"/>
            </div>
        </div>
    </div>
</template>

<style scoped></style>