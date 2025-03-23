<template>
  <NavBar />
  <main>
    <router-view />
  </main>
</template>

<script setup lang="ts">
import NavBar from './components/NavBar.vue'
</script>


<style scoped>
main {
  padding: 2rem;
  font-family: sans-serif;
}
</style>
