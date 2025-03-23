<template>
    <div class="random-chart">
      <h2>🎲 Random Seaborn Chart</h2>
      <p>Kattints a gombra és nézd meg, milyen meglepetést generálunk!</p>
  
      <button @click="generateRandomChart">Generate Random Chart</button>
  
      <div v-if="imageSrc" class="chart-wrapper">
        <img :src="imageSrc" alt="Random Seaborn Chart" />
  
        <div class="meta">
          <p><strong>Típus:</strong> {{ current.chartType }}</p>
          <p><strong>Dataset:</strong> {{ current.dataset }}</p>
          <p v-if="current.x"><strong>X tengely:</strong> {{ current.x }}</p>
          <p v-if="current.y"><strong>Y tengely:</strong> {{ current.y }}</p>
          <p><strong>Paletta:</strong> {{ current.palette }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue'
  import { generatePlot } from '@/services/plotService'
  import type { PlotRequest } from '@/types/plot'
  
  const imageSrc = ref('')
  const current = ref<PlotRequest>({
    chartType: '',
    dataset: '',
    x: '',
    y: '',
    palette: ''
  })
  
  const chartTypes = ['bar', 'violin', 'heatmap']
  const datasets = {
    tips: ['day', 'time', 'sex', 'total_bill', 'tip'],
    iris: ['species', 'sepal_length', 'petal_length', 'petal_width'],
    penguins: ['species', 'island', 'flipper_length_mm', 'body_mass_g']
  }
  const palettes = ['deep', 'muted', 'pastel', 'dark', 'colorblind']
  
  function getRandom<T>(arr: T[]): T {
    return arr[Math.floor(Math.random() * arr.length)]
  }
  
  async function generateRandomChart() {
    const chartType = getRandom(chartTypes)
    const dataset = getRandom(Object.keys(datasets)) as keyof typeof datasets
    const palette = getRandom(palettes)
    const x = chartType === 'heatmap' ? undefined : getRandom(datasets[dataset])
    const y = chartType === 'heatmap' ? undefined : getRandom(datasets[dataset].filter(k => k !== x))
  
    const req: PlotRequest = {
      chartType,
      dataset,
      x,
      y,
      palette
    }
  
    current.value = req
    imageSrc.value = await generatePlot(req)
  }
  </script>
  
  <style scoped>
  .random-chart {
    text-align: center;
    padding: 2rem;
    max-width: 800px;
    margin: 0 auto;
  }
  
  button {
    padding: 0.75rem 1.5rem;
    background-color: #f59e0b;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 0.5rem;
    cursor: pointer;
    margin: 1.5rem 0;
    transition: background-color 0.3s;
  }
  button:hover {
    background-color: #d97706;
  }
  
  .chart-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }
  
  .chart-wrapper img {
    max-width: 100%;
    border-radius: 1rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
  
  .meta {
    background-color: #f9fafb;
    padding: 1rem 1.5rem;
    border-radius: 0.75rem;
    text-align: left;
    font-size: 0.95rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  }
  </style>