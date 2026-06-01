<script setup lang="ts">
    import { useRoute } from 'vue-router';
    import { ref, onMounted, computed } from 'vue'
    import { type EnvironmentHistoryPublic, type EnvironmentProfilePublic, type EnvironmentPublic } from '@/api/types.gen';
    import {    Environment as EnvironmentService, 
                EnvironmentHistory as EnvironmentHistoryService,
                EnvironmentProfile as EnvironmentProfileService,
                Live as LiveService } from '@/api/sdk.gen';
    import EnvironmentHistorySnapshot from '@/components/EnvironmentHistorySnapshot.vue';
    import LiveChart from '@/components/LiveChart.vue';
    import { useLiveCache } from '@/composables/useLiveCache';
    import type { AlignedData } from 'uplot';

    const route = useRoute()
    const id = computed(() => parseInt(route.params.id as string))

    const environment = ref<EnvironmentPublic>();
    const environmentProfile = ref<EnvironmentProfilePublic>();
    const environmentHistoryLatest = ref<EnvironmentHistoryPublic>();
    const loading = ref(false);
    const error = ref<string | null>(null);

    const liveTemps = useLiveCache<EnvironmentHistoryPublic>(
        (t) => t.temperature!,
        (t) => t.datetime,
        1 * 60 * 1000 // 1min
    )

    const liveTempAlignedData = computed<AlignedData>(() => {
        const timestamps = liveTemps.items.value.map((t) => t.datetime);
        const temps = liveTemps.items.value.map((t) => t.temperature ?? NaN);
        return [timestamps, temps];
    });

    onMounted(() => {
        loadEnvironment();
        const ws = new WebSocket('ws://localhost:8000/live/ws/environment-history/' + id.value);
        ws.onopen = () => {
            console.log('WebSocket connected');
        };
        ws.onmessage = (event) => {
            let msgObject = JSON.parse(event.data);
            environmentHistoryLatest.value = msgObject;
            liveTemps.add(msgObject);
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
            error.value = err.message || 'Error loading environment ' + id;
        }
        finally {
            loading.value = false;
            if(environment.value?.environment_profile_id !== null) {
                await Promise.all([loadActiveProfile(), loadHistoryCacheFromServer()]);
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

    async function loadHistoryCacheFromServer() {
        try {
            const { data } = await LiveService.getLiveEnvironmentHistoryByGroupLiveEnvironmentHistoryEnvironmentIdGet({
                path: { environmentId: id.value }
            });
            if(data && data.length > 0) {
                environmentHistoryLatest.value = data[data.length - 1];
                data.forEach((record) => liveTemps.add(record));
            }
        }
        catch(err: any) {
            //
            console.error(err);
        }
        finally {
            //
        }
    }

    /**
     * Loads the most recent EnvironmentHistory record
     * @deprecated Use `loadHistoryCacheFromServer()` instead
     */
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

    const opts: uPlot.Options = {
        width: 999,
        height: 300,
        series: [
            {},
            {
                label: "Temp",
                stroke: "red",
            },
        ],
    };

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
        <div>
            <LiveChart :data="liveTempAlignedData" :opts="opts"></LiveChart>
        </div>
        <div class="hidden">
            {{ environmentHistoryLatest }}
        </div>
    </div>
    
</template>

<style scoped></style>