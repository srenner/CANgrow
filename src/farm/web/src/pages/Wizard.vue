<script setup lang="ts">
    import { ref, onMounted } from 'vue';

    const step = ref(1);

    const hasCrops = ref(false);
    const hasPlants = ref(false);
    const hasEnvironments = ref(false);

    const cropName = ref('');


    onMounted(() => {
        //check for crop table
        //if none, prompt 1

        //check for plant table
        //if none, prompt 1 then 2

        //check for environment table
        // if none, prompot 1 then 2 then 3
    });


    function addCrop() {
        //add crop to database
    }


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


        <div v-if="!hasCrops">
            <h2>Let's get growing.</h2>

            <div>
                <p>Start by naming your crop</p>
                <div>
                    <label for="crop-name">Crop Name:</label>
                    <input type="text" id="crop-name" name="crop-name" v-model="cropName"
                    class="border dark:bg-gray-600 bg-gray-200 border-gray-300 rounded px-3 py-2 w-full">
                    
                </div>
                <button @click="nextStep">Add Crops</button>
            </div>
        </div>


<!-- 
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
        </div> -->
    </div>
</template>