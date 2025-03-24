<template>
    <section class="distribution-demo">
      <div class="content-wrapper">
        <!-- Left side: explanation + form -->
        <div class="left-panel">
          <h2>Distribution Visualization</h2>
          <p class="description">
            Seaborn makes it easy to visualize the <strong>distribution</strong> of your data — far beyond basic barplots.
          </p>
          <p>
            Try <strong>violinplot</strong> or <strong>boxplot</strong> to explore spread, median, and density with minimal code.
          </p>
  
          <div class="controls">
            <label>
              Chart type:
              <select v-model="chartType">
                <option value="violin">Violin</option>
                <option value="box">Box</option>
              </select>
            </label>
  
            <label>
              X axis:
              <select v-model="x">
                <option value="day">day</option>
                <option value="sex">sex</option>
                <option value="smoker">smoker</option>
                <option value="time">time</option>
              </select>
            </label>
  
            <label>
              Y axis:
              <select v-model="y">
                <option value="total_bill">total_bill</option>
                <option value="tip">tip</option>
                <option value="size">size</option>
              </select>
            </label>
  
            <button @click="generateChart">Generate</button>
          </div>
  
          <p class="note">
            ✅ In just one line, Seaborn shows medians, quartiles, spread, and even kernel density (violinplot).
          </p>
        </div>
  
        <!-- Right side: chart + code -->
        <div class="right-panel">
          <transition name="fade">
            <img v-if="imageSrc" :src="imageSrc" alt="Distribution Chart" class="chart-img" />
          </transition>
  
          <p class="commentary">
            This <strong>{{ chartType }}</strong> plot shows how <code>{{ y }}</code> varies across <code>{{ x }}</code>.
          </p>
  
          <pre class="code-block">
  <code><span class="line">1  </span><span class="keyword">import</span> seaborn <span class="keyword">as</span> sns
  <span class="line">2  </span>sns.set_theme(style=<span class="highlight">"darkgrid"</span>)
  <span class="line">3  </span>sns.{{ chartType }}plot(x=<span class="highlight">"{{ x }}"</span>, y=<span class="highlight">"{{ y }}"</span>, data=<span class="highlight">tips</span>, palette=<span class="highlight">"mako"</span>)</code>
          </pre>
        </div>
      </div>
    </section>
  </template>
  
  <script setup lang="ts">
  import { ref, watchEffect } from 'vue'
  import type { PlotRequest } from '@/types/plot'
  
  const x = ref('day')
  const y = ref('total_bill')
  const chartType = ref<'violin' | 'box'>('violin')
  const imageSrc = ref('')
  
  async function generateChart() {
    const request: PlotRequest = {
      chartType: chartType.value,
      dataset: 'tips',
      x: x.value,
      y: y.value,
      palette: 'muted'
    }
  
    const response = await fetch('http://localhost:8000/generate-plot?theme=whitegrid', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(request)
    })
  
    const data = await response.json()
    imageSrc.value = data.image
  }
  
  watchEffect(() => {
    generateChart()
  })
  </script>
  
  <style scoped>
  .distribution-demo {
    padding: 3rem 4vw;
    max-width: 1600px;
    margin: 0 auto;
    text-align: left;
  }
  
  .content-wrapper {
    display: flex;
    flex-direction: row;
    gap: 5rem;
    flex-wrap: nowrap;
    align-items: flex-start;
    justify-content: space-between;
  }
  
  .left-panel {
    flex: 0 0 35%;
    max-width: 35%;
    min-width: 300px;
  }
  
  .right-panel {
    flex: 0 0 60%;
    max-width: 60%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  h2 {
    font-size: 1.8rem;
    margin-bottom: 1rem;
  }
  
  .description {
    font-size: 1rem;
    margin-bottom: 1rem;
    color: #cbd5e1;
  }
  
  .controls {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-top: 1.5rem;
    margin-bottom: 1rem;
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
    background-color: #6366f1;
    color: white;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  button:hover {
    background-color: #4f46e5;
  }
  
  .note {
    margin-top: 1rem;
    font-size: 0.95rem;
    color: #a5b4fc;
    font-style: italic;
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
  }
  
  .code-block .line {
    display: inline-block;
    width: 2rem;
    color: #6b7280;
  }
  
  .code-block .highlight {
    color: #facc15;
    font-weight: bold;
  }
  
  .code-block .keyword {
    color: #60a5fa;
    font-weight: bold;
  }
  </style>
  