<script setup lang="ts">
    import { ref, onMounted } from 'vue'
    import { ArrowPathIcon, MoonIcon, SunIcon } from '@heroicons/vue/24/solid'
    import { createClient } from '@/api/client';
    import type { Environment } from '@/api/types.gen';
    import { Environment as EnvironmentService } from '@/api/sdk.gen';


    const dark = ref<boolean>(false);

    function  applyTheme(dark:boolean) {
        const root = document.documentElement;
        root.classList.toggle('dark', dark);
  }

    onMounted(() => {
        const saved = localStorage.getItem('theme');
        if(saved) {
            dark.value = saved === 'dark';
        }
        else {
            dark.value = window.matchMedia('(prefers-color-scheme: dark)').matches;
        }
        applyTheme(dark.value);
    });

    function toggleTheme(): void {
        dark.value = !dark.value;
        applyTheme(dark.value);
        localStorage.setItem('theme', dark.value ? 'dark': 'light');
    }

</script>

<template>
    <header>
        CANgrow
        <button @click="toggleTheme">
            <span v-if="dark">
                <SunIcon class="size-6"></SunIcon>
            </span>
            <span v-else>
                <MoonIcon class="size-6"></MoonIcon>
            </span>
        </button>
        
    </header>
</template>

<style scoped></style>
