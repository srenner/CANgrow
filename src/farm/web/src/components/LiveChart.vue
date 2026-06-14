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
        const processedData: any[] = [[...props.data[0].map(t => t / 1000)], props.data[1]];
        plot = new uPlot(props.opts, processedData, chart.value);
    }, { deep: true })

    // ### END WATCHERS ###

</script>

<template>
    <div ref="chart"></div>
</template>

