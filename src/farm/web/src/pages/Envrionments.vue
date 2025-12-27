<script setup lang="ts">
    import { ref, onMounted } from 'vue'
    import { ArrowPathIcon, MoonIcon, SunIcon } from '@heroicons/vue/24/solid'
    import { createClient } from '@/api/client';
    import type { Environment } from '@/api/types.gen';
    import { Environment as EnvironmentService } from '@/api/sdk.gen';

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
    <div>
        <div v-if="loading">Loading...</div>
        <div v-else-if="error">{{ error }}</div>
        <ul v-else>
            <li v-for="env in environments" :key="env.id!">
                {{ env }}
            </li>
        </ul>
    </div>
</template>

<style scoped></style>