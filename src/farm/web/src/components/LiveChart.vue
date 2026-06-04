<script setup lang="ts">
    import { ref, onMounted, onBeforeUnmount, watch } from 'vue';
    import uPlot, { type AlignedData } from 'uplot';
    import 'uplot/dist/uPlot.min.css';

    const props = defineProps<{
        data: AlignedData;
        opts: uPlot.Options;
    }>();

    const chart = ref<HTMLDivElement>();
    let plot : uPlot | null = null;

    // ### LIFECYCLE #######

    onMounted(() => {
        plot = new uPlot(props.opts, props.data, chart.value);        
    });

    onBeforeUnmount(() => {
        plot?.destroy();
    });

    // ### END LIFECYCLE ###

    // ### WATCHERS #######

    watch(() => [props.data, props.opts], () => {
        plot?.destroy();
        plot = new uPlot(props.opts, props.data, chart.value);
    }, { deep: true })

    // ### END WATCHERS ###

</script>

<template>
    <div ref="chart"></div>
</template>

