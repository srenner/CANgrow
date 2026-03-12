<script setup lang="ts">
    import { ref, onMounted } from 'vue';

    const step = ref(1);

    function nextStep() {
        step.value++;
    }

    function prevStep() {
        step.value--;
    }
</script>

<template>
    <h1>Wizard</h1>
    <div>
        <div v-if="step === 1">
            <p>Step 1: Welcome to the wizard!</p>
            <button @click="nextStep">Next</button>
        </div>
        <div v-else-if="step === 2">
            <p>Step 2: This is the second step.</p>
            <button @click="prevStep">Previous</button>
            <button @click="nextStep">Next</button>
        </div>
        <div v-else-if="step === 3">
            <p>Step 3: This is the final step.</p>
            <button @click="prevStep">Previous</button>
            <button @click="nextStep">Finish</button>
        </div>
        <div v-else-if="step === 4">
            <p>Wizard completed! Thank you.</p>
        </div>
    </div>
</template>