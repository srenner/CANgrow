<script setup lang="ts">
    import { useRoute } from 'vue-router';
    import { ref, onMounted, computed } from 'vue'
    import { type EnvironmentHistoryPublic, type EnvironmentProfilePublic, type EnvironmentPublic } from '@/api/types.gen';
    import { Environment as EnvironmentService, EnvironmentProfile as EnvironmentProfileService, EnvironmentHistory as EnvironmentHistoryService } from '@/api/sdk.gen';
    import EnvironmentHistorySnapshot from '@/components/EnvironmentHistorySnapshot.vue';

    const route = useRoute()
    const id = computed(() => parseInt(route.params.id as string))

    const environment = ref<EnvironmentPublic>();
    const environmentProfile = ref<EnvironmentProfilePublic>();
    const environmentHistoryLatest = ref<EnvironmentHistoryPublic>();
    const loading = ref(false);
    const error = ref<string | null>(null);
    let messages: any = ref<string[]>([]);

    onMounted(() => {
        loadEnvironment();
        const ws = new WebSocket('ws://localhost:8000/live/ws/environment-history/' + id.value);
        ws.onopen = () => {
            console.log('WebSocket connected');
        };
        ws.onmessage = (event) => {
            messages.value.push(JSON.parse(event.data));
            console.log('Message received:', event.data);
        };
        ws.onerror = (error) => {
            console.error('WebSocket error:', error);
        };
        ws.onclose = (event) => {
            console.log('WebSocket closed:', event.code, event.reason);
        };
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
                await loadLatestHistory();
            }
        }
    }

    async function loadActiveProfile() {
        try {
            const { data } = await EnvironmentProfileService.getEnvironmentProfile({ path: { id: environment.value?.environment_profile_id! } });
            environmentProfile.value = data;
        }
        catch(err: any) {
            console.error(err);
        }
        finally {
            // 
        }
    }

    async function loadLatestHistory() {
        try {
            const { data } = await EnvironmentHistoryService.getLatestEnvironmentHistory({path: { environmentId: id.value }})
            environmentHistoryLatest.value = data;
        }
        catch(err: any) {
            //
            console.error(err);
        }
        finally {
            //
        }
    }

</script>

<template>
    
    <h1>
        <span><strong>ENVIRONMENT:</strong> {{ environment?.name }}</span>
        <span v-if="environment?.descr">{{ ' - ' + environment.descr }}</span>
    </h1>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
        <div>
            <strong>ACTIVE PROFILE:</strong> {{ environmentProfile?.name }} - {{ environmentProfile?.descr }}
        </div>
        <div>
            <EnvironmentHistorySnapshot :record="environmentHistoryLatest" />
        </div>
        <div class="hidden">
            {{ environment }}
        </div>
        <div class="hidden">
            {{ environmentHistoryLatest }}
        </div>
        <div>
            websocket: {{ messages }}
        </div>
    </div>
    
</template>

<style scoped></style>