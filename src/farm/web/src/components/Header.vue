<script setup lang="ts">
    import { ref, onMounted } from 'vue'
    import { MoonIcon, SunIcon } from '@heroicons/vue/24/solid'
    import { useDarkMode } from '../composables/useDarkMode';
    const { isDark, toggleDark } = useDarkMode();

</script>

<template>
    <header>
        CANgrow
        <button @click="toggleDark">
            <span v-if="isDark">
                <SunIcon class="size-6"></SunIcon>
            </span>
            <span v-else>
                <MoonIcon class="size-6"></MoonIcon>
            </span>
        </button>
        {{ isDark }}
        
    </header>

    <hr class="mt-2 mb-2">
</template>

<style scoped></style>
