<script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import Header from './components/Header.vue';

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
  <Header />
  <RouterView />
</template>

<style scoped></style>
