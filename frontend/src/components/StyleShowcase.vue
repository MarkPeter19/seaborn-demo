<template>
    <section class="style-showcase">
      <div class="content-wrapper">
        <!-- Left side: text + form -->
        <div class="left-panel">
          <h2>🎨 Theme & Palette Showcase</h2>
          <p class="description">
            Choose a theme and palette to see how the chart changes in Seaborn!
          </p>
  
          <div class="controls">
            <label>
              Theme:
              <select v-model="theme">
                <option value="whitegrid">whitegrid</option>
                <option value="darkgrid">darkgrid</option>
                <option value="ticks">ticks</option>
                <option value="white">white</option>
                <option value="dark">dark</option>
              </select>
            </label>
  
            <label>
              Palette:
              <select v-model="palette">
                <option value="deep">deep</option>
                <option value="muted">muted</option>
                <option value="pastel">pastel</option>
                <option value="dark">dark</option>
                <option value="colorblind">colorblind</option>
                <option value="rocket">rocket</option>
                <option value="mako">mako</option>
                <option value="flare">flare</option>
                <option value="crest">crest</option>
                <option value="coolwarm">coolwarm</option>
                <option value="viridis">viridis</option>
                <option value="magma">magma</option>
                <option value="inferno">inferno</option>
                <option value="cividis">cividis</option>
                <option value="Set2">Set2</option>
                <option value="tab10">tab10</option>
                <option value="cubehelix">cubehelix</option>
              </select>
            </label>
  
            <button @click="generateChart">Refresh</button>
          </div>
        </div>
  
        <!-- Right side: image + code -->
        <div class="right-panel">
          <transition name="fade">
            <img v-if="imageSrc" :src="imageSrc" alt="Styled Seaborn Chart" class="chart-img" />
          </transition>
  
          <p class="commentary">
            This is a <strong>{{ theme }}</strong> themed <strong>barplot</strong> with the <strong>{{ palette }}</strong> palette.
          </p>
  
          <pre class="code-block">
  <code><span class="line">1  </span>import seaborn as sns
  <span class="line">2  </span>sns.set_theme(style=<span class="highlight">"{{ theme }}"</span>)
  <span class="line">3  </span>sns.barplot(x="day", y="total_bill", data=tips, palette=<span class="highlight">"{{ palette }}"</span>)</code>
          </pre>
        </div>
      </div>
    </section>
  </template>
  
  <script setup lang="ts">
  import { ref, watchEffect } from 'vue'
  import type { PlotRequest } from '@/types/plot'
  import { generatePlot } from '@/services/plotService'
  
  const theme = ref('whitegrid')
  const palette = ref('deep')
  const imageSrc = ref('')
  
  async function generateChart() {
    const request: PlotRequest = {
      chartType: 'bar',
      dataset: 'tips',
      x: 'day',
      y: 'total_bill',
      palette: palette.value,
    }
  
    const response = await fetch('http://localhost:8000/generate-plot?theme=' + theme.value, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(request),
    })
  
    const data = await response.json()
    imageSrc.value = data.image
  }
  
  watchEffect(() => {
    generateChart()
  })
  </script>
  
  <style scoped>
  .style-showcase {
    padding: 3rem 5vw;
    max-width: 100%;
    margin: 0 auto;
    text-align: left;
  }
  
  .content-wrapper {
    display: flex;
    flex-direction: row;
    gap: 4rem;
    flex-wrap: wrap;
    align-items: flex-start;
    justify-content: center;
  }
  
  .left-panel {
    flex: 1;
    min-width: 300px;
    max-width: 400px;
  }
  
  .right-panel {
    flex: 2;
    min-width: 400px;
    max-width: 1000px;
  }
  
  .description {
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
  }
  
  .controls {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-bottom: 2rem;
  }
  
  label {
    display: flex;
    flex-direction: column;
    font-weight: 500;
    gap: 0.25rem;
  }
  
  select,
  button {
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    border: 1px solid #cbd5e1;
    font-size: 1rem;
  }
  
  button {
    background-color: #7DB0BC;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  button:hover {
    background-color: #7DB0BC;
  }
  
  .chart-img {
    width: 100%;
    max-width: 100%;
    border-radius: 1rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    margin-bottom: 1rem;
  }
  
  .commentary {
    font-size: 1rem;
    color: #7DB0BC;
    margin-bottom: 1rem;
  }
  
  .code-block {
    background-color: #1e1e1e;
    color: #e5e7eb;
    text-align: left;
    padding: 1rem;
    border-radius: 0.5rem;
    font-family: 'Courier New', monospace;
    font-size: 0.95rem;
    white-space: pre-wrap;
    border: 1px solid #374151;
    overflow-x: auto;
    line-height: 1.5;
    width: 100%;
    max-width: 100%;
  }
  
  .code-block .line {
    display: inline-block;
    width: 2rem;
    color: #6b7280;
  }
  
  .code-block .highlight {
    color: #15fa78;
    font-weight: bold;
  }
  
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }
  </style>