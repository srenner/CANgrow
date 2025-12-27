<script setup lang="ts">
    import { ref, onMounted } from 'vue'
    import { ArrowPathIcon, MoonIcon, SunIcon } from '@heroicons/vue/24/solid'
    import { createClient } from '@/api/client';

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

    const api = createClient();
    const environments = ref([]);
    const loading = ref(false);
    const error = ref<string | null>(null);

    async function loadEnvironments() {
        loading.value = true;
        error.value = null;
        try {
            //const response = con

        }
        catch {

        }
    }

    function toggleTheme(): void {
        dark.value = !dark.value;
        applyTheme(dark.value);
        localStorage.setItem('theme', dark.value ? 'dark': 'light');
    }

</script>

<template>
    <header>
        <button @click="toggleTheme">
            <span v-if="dark">
                <SunIcon class="size-6"></SunIcon>
            </span>
            <span v-else>
                <MoonIcon class="size-6"></MoonIcon>
            </span>
        </button>
        <div>
            <div v-if="loading">Loading...</div>
            <div v-else-if="error">{{ error }} }}</div>
            <ul v-else>
                <li v-for="env in environments" :key="env.id">
                    {{ env.name }}
                </li>
            </ul>
        </div>
    </header>
</template>

<style scoped></style>
