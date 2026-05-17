<script setup>
    import { ref, onMounted, onBeforeUnmount, watch } from 'vue';
    import uPlot from 'uplot';
    import 'uplot/dist/uPlot.min.css';

    const props = defineProps({
        data: {
            type: Array,
            required: true
        },
        opts: {
            type: Object,
            required: true
        }
    });

    const chart = ref(null);
    let plot = null;

    let chartData = [
        props.data.map((_,i) => i),
        props.data
    ];

    // ### LIFECYCLE #######

    onMounted(() => {
        plot = new uPlot(props.opts, chartData, chart.value);        
    });

    onBeforeUnmount(() => {
        plot?.destroy();
    });

    // ### END LIFECYCLE ###

    // ### WATCHERS #######

    watch(() => props.data, (newData) => {
        let chartData = [
            newData.map((_,i) => i),
            newData
        ]
        plot?.setData(chartData)
    }, { deep: true });

    watch(() => props.opts, (newOpts) => {
        plot?.destroy();
        plot = new uPlot(newOpts, props.data, chart.value);
    }, { deep: true })

    // ### END WATCHERS ###



</script>

<template>
    <div ref="chart"></div>
</template>