<script setup lang="ts">
    import { useDateFormatter } from '@/composables/useDateFormatter';
    const props = defineProps(['record']);
    const { formatDate } = useDateFormatter();

    // get environment history

    /*
        id: int | None = Field(default=None, primary_key=True)
        environment_id: int | None = Field(default=None, foreign_key="environment.id")
        light_status: bool | None
        heat_status: bool | None
        temperature: float | None
        humidity: float | None
        gas: float | None
        datetime: int = Field(default=int(time.time()))
    */

    // use the history record datetime instead
    const now = new Date(1767408837 * 1000).toLocaleString();



</script>

<template>
    <div v-if="record">
        light: {{ record.light_status }}
        <br>
        heat: {{ record.heat_status }}
        <br>
        temp: {{ record.temperature.toFixed(1) }}
        <br>
        humid: {{ record.humidity.toFixed(1) }}
        <br>
        as of {{ formatDate(record.datetime) }}
    </div>
</template>

<style scoped>

</style>