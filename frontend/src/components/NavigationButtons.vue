<template>
    <div class="nav-buttons">
      <button v-if="onPrev" class="nav-btn secondary" @click="onPrev">Back</button>
      <button v-if="onNext" class="nav-btn" @click="onNext">Next</button>
    </div>
  </template>
  
  <script setup lang="ts">
  defineProps<{
    onNext?: () => void
    onPrev?: () => void
  }>()
  </script>
  
  <style scoped>
  .nav-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 2rem;
  }
  
  .nav-btn {
    padding: 0.6rem 1.5rem;
    font-size: 1rem;
    font-weight: bold;
    border-radius: 0.5rem;
    border: none;
    background-color: #6da7ee;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .nav-btn:hover {
    background-color: #3babc4;
  }
  
  .nav-btn.secondary {
    background-color: #4c4f54;
  }
  
  .nav-btn.secondary:hover {
    background-color: #3b434e;
  }
  </style>
  