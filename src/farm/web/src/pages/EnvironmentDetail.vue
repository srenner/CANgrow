<script setup lang="ts">
    import { useRoute } from 'vue-router';
    import { ref, onMounted, computed } from 'vue'
    import { type EnvironmentProfilePublic, type EnvironmentPublic } from '@/api/types.gen';
    import { Environment as EnvironmentService, EnvironmentProfile as EnvironmentProfileService } from '@/api/sdk.gen';
    import EnvironmentHistoryLatest from '@/components/EnvironmentHistoryLatest.vue';

    const route = useRoute()
    const id = computed(() => parseInt(route.params.id as string))

    const environment = ref<EnvironmentPublic>();
    const environmentProfile = ref<EnvironmentProfilePublic>();
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
            environment.value = data;
        }
        catch(err: any) {
            error.value = err.message || 'Error loading environment ' + id

        }
        finally {
            loading.value = false;
            if(environment.value?.environment_profile_id !== null) {
                await loadActiveProfile();
            }
        }
    }

    async function loadActiveProfile() {
        try {
            const { data } = await EnvironmentProfileService.getEnvironmentProfile({ path: { id: environment.value?.environment_profile_id! } });
            environmentProfile.value = data;
        }
        catch(err: any) {
            //
        }
        finally {
            // 
        }
    }

</script>

<template>
    
    <h1>{{ environment?.name }}</h1>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
        <div class="font-mono p-5">
            <div>
                {{ environment }}
            </div>
            <div>
                {{ environmentProfile }}
            </div>
        </div>
        <div>
            <EnvironmentHistoryLatest />
        </div>
    </div>
    
</template>

<style scoped></style>