<template>
    <div class="playground">
      <div class="control-panel">
        <h2>Chart Playground 🎛️</h2>
  
        <label>
          Chart Type
          <select v-model="form.chartType">
            <option value="bar">Bar</option>
            <option value="violin">Violin</option>
            <option value="scatter">Scatter</option>
            <option value="heatmap">Heatmap</option>
          </select>
        </label>
  
        <label>
          Dataset
          <select v-model="form.dataset">
            <option value="tips">Tips</option>
            <option value="iris">Iris</option>
            <option value="penguins">Penguins</option>
          </select>
        </label>
  
        <label v-if="form.chartType !== 'heatmap'">
          X Axis
          <input v-model="form.x" type="text" placeholder="e.g. day" />
        </label>
  
        <label v-if="form.chartType !== 'heatmap'">
          Y Axis
          <input v-model="form.y" type="text" placeholder="e.g. total_bill" />
        </label>
  
        <label>
          Color Palette
          <select v-model="form.palette">
            <option value="deep">deep</option>
            <option value="muted">muted</option>
            <option value="pastel">pastel</option>
            <option value="dark">dark</option>
            <option value="colorblind">colorblind</option>
          </select>
        </label>
  
        <button @click="submitForm">Generate</button>
      </div>
  
      <div class="plot-view">
        <transition name="fade">
          <img v-if="imageSrc" :src="imageSrc" alt="Generated Seaborn Chart" class="chart-image" />
        </transition>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue'
  import { generatePlot } from '@/services/plotService'
  import type { PlotRequest } from '@/types/plot'
  
  const form = ref<PlotRequest>({
    chartType: 'bar',
    dataset: 'tips',
    x: 'day',
    y: 'total_bill',
    palette: 'deep'
  })
  
  const imageSrc = ref('')
  
  async function submitForm() {
    try {
      imageSrc.value = '' // reset to trigger transition
      const result = await generatePlot(form.value)
      setTimeout(() => {
        imageSrc.value = result
      }, 100) // small delay to trigger fade-in
    } catch (error) {
      console.error('Failed to generate plot:', error)
    }
  }
  </script>
  
  <style scoped>
  .playground {
    display: flex;
    flex-direction: row;
    gap: 2rem;
    padding: 2rem;
    justify-content: center;
    align-items: flex-start;
    flex-wrap: wrap;
  }
  
  .control-panel {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    background: #f8fafc;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    min-width: 300px;
    max-width: 400px;
    flex: 1;
  }
  
  .control-panel h2 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
    color: #1f2937;
  }
  
  label {
    display: flex;
    flex-direction: column;
    font-weight: 500;
    gap: 0.3rem;
  }
  
  select,
  input {
    padding: 0.5rem;
    border-radius: 0.5rem;
    border: 1px solid #cbd5e1;
  }
  
  button {
    padding: 0.75rem;
    border: none;
    background-color: #3b82f6;
    color: white;
    font-weight: bold;
    border-radius: 0.5rem;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #2563eb;
  }
  
  .plot-view {
    flex: 2;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 400px;
    max-width: 600px;
    width: 100%;
  }
  
  .chart-image {
    max-width: 100%;
    border-radius: 1rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    animation: fadein 0.8s ease;
  }
  
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter-from, .fade-leave-to {
    opacity: 0;
  }
  </style>