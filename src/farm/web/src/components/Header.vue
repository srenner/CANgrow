<script setup lang="ts">
    import { ref, onMounted } from 'vue'
    import { MoonIcon, SunIcon } from '@heroicons/vue/24/solid'
    import { useDarkMode } from '../composables/useDarkMode';
    const { isDark, toggleDark } = useDarkMode();
</script>

<template>
    <div class="navbar bg-base-100 shadow-sm">
        <div class="flex-none">
            <button class="btn btn-square btn-ghost">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block h-5 w-5 stroke-current">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>
        </div>
        <div class="flex-1">
            <a class="btn btn-ghost text-xl">CANgrow</a>
        </div>
        <div class="flex-none">
            <button class="btn btn-square btn-ghost" @click="toggleDark">
            <span v-if="isDark">
                <SunIcon class="size-6"></SunIcon>
            </span>
            <span v-else>
                <MoonIcon class="size-6"></MoonIcon>
            </span>

            </button>
        </div>
    </div>
</template>

<style scoped></style>
