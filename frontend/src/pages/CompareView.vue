<template>
    <div class="compare-view">
      <h2 class="title">Seaborn vs Matplotlib</h2>
      <p class="subtitle">Húzd a csúszkát és nézd meg a különbséget!</p>
  
      <div class="slider-container">
        <div class="image-wrapper">
          <img :src="matplotlibImage" alt="Matplotlib Chart" class="image underneath" />
          <div class="image-overlay" :style="{ width: sliderValue + '%' }">
            <img :src="seabornImage" alt="Seaborn Chart" class="image" />
          </div>
        </div>
  
        <input
          type="range"
          min="0"
          max="100"
          v-model="sliderValue"
          class="slider"
        />
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue'
  
  const sliderValue = ref(50)
  const matplotlibImage = ref('')
  const seabornImage = ref('')
  
  async function fetchComparisonImages() {
    try {
      const res = await fetch('http://localhost:8000/compare-plot')
      const data = await res.json()
      matplotlibImage.value = data.matplotlib
      seabornImage.value = data.seaborn
    } catch (err) {
      console.error('Error fetching comparison images:', err)
    }
  }
  
  onMounted(() => {
    fetchComparisonImages()
  })
  </script>
  
  <style scoped>
  .compare-view {
    padding: 2rem;
    text-align: center;
  }
  
  .title {
    font-size: 2rem;
    margin-bottom: 0.5rem;
  }
  
  .subtitle {
    font-size: 1.1rem;
    margin-bottom: 2rem;
    color: #64748b;
  }
  
  .slider-container {
    position: relative;
    width: 100%;
    max-width: 700px;
    margin: 0 auto;
  }
  
  .image-wrapper {
    position: relative;
    width: 100%;
    overflow: hidden;
    border-radius: 1rem;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15);
  }
  
  .image {
    display: block;
    width: 100%;
    height: auto;
    user-select: none;
  }
  
  .image.underneath {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 0;
  }
  
  .image-overlay {
    position: relative;
    overflow: hidden;
    z-index: 1;
  }
  
  .slider {
    margin-top: 1rem;
    width: 100%;
    accent-color: #3b82f6;
  }
  </style>
  