<template>
    <section class="aggregation-demo">
      <div class="content-wrapper">
        <!-- Left side: explanation + form -->
        <div class="left-panel">
          <h2>Barplot Aggregation Demo</h2>
          <p class="description">
            Unlike Matplotlib, Seaborn <strong>automatically groups</strong> and <strong>aggregates</strong> your data by the x-axis categories.
          </p>
          <p>
            For example, here we show the <code>mean</code> of <strong>total_bill</strong> for each <strong>day</strong> in the dataset.
          </p>
  
          <div class="controls">
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
            ✅ No need to calculate means manually – Seaborn does it for you!
          </p>
        </div>
  
        <!-- Right side: chart + code -->
        <div class="right-panel">
          <transition name="fade">
            <img v-if="imageSrc" :src="imageSrc" alt="Aggregated Chart" class="chart-img" />
          </transition>
  
          <p class="commentary">
            This barplot shows the <strong>mean</strong> of <code>{{ y }}</code> for each <code>{{ x }}</code>.
          </p>
  
          <pre class="code-block">
  <code><span class="line">1  </span><span class="keyword">import</span> seaborn <span class="keyword">as</span> sns
  <span class="line">2  </span>sns.set_theme(style=<span>"darkgrid"</span>)
  <span class="line">3  </span>sns.barplot(x=<span class="highlight">"{{ x }}"</span>, y=<span class="highlight">"{{ y }}"</span>, data=<span class="highlight">tips</span>, palette=<span>"magma"</span>)</code>
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
  const imageSrc = ref('')
  
  async function generateChart() {
    const request: PlotRequest = {
      chartType: 'bar',
      dataset: 'tips',
      x: x.value,
      y: y.value,
      palette: 'magma'
    }
  
    const response = await fetch('http://localhost:8000/generate-plot?theme=darkgrid', {
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
  .aggregation-demo {
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
    background-color: #10b981;
    color: white;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  button:hover {
    background-color: #059669;
  }
  
  .note {
    margin-top: 1rem;
    font-size: 0.95rem;
    color: #4ade80;
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
    color: #15faae;
    font-weight: bold;
  }
  
  .code-block .keyword {
    color: #60a5fa;
    font-weight: bold;
  }
  </style>
  