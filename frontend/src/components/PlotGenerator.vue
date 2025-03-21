<template>
  <div class="plot-generator">
    <h2>📊 Generate Seaborn Plot</h2>

    <form @submit.prevent="submitForm" class="form">
      <label>
        Chart Type:
        <select v-model="form.chartType">
          <option value="bar">Bar</option>
          <option value="violin">Violin</option>
          <option value="heatmap">Heatmap</option>
        </select>
      </label>

      <label>
        Dataset:
        <select v-model="form.dataset">
          <option value="tips">tips</option>
          <option value="iris">iris</option>
          <option value="penguins">penguins</option>
        </select>
      </label>

      <label v-if="form.chartType !== 'heatmap'">
        X:
        <input v-model="form.x" type="text" placeholder="e.g. day" />
      </label>

      <label v-if="form.chartType !== 'heatmap'">
        Y:
        <input v-model="form.y" type="text" placeholder="e.g. total_bill" />
      </label>

      <label>
        Palette:
        <input v-model="form.palette" type="text" placeholder="e.g. deep" />
      </label>

      <button type="submit">Generate</button>
    </form>

    <div v-if="imageSrc" class="image-preview">
      <img :src="imageSrc" alt="Seaborn Plot" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { generatePlot } from "@/services/plotService";
import type { PlotRequest } from "@/types/plot";

const form = ref<PlotRequest>({
  chartType: "bar",
  dataset: "tips",
  x: "day",
  y: "total_bill",
  palette: "deep",
});

const imageSrc = ref("");

async function submitForm() {
  try {
    imageSrc.value = await generatePlot(form.value);
  } catch (error) {
    console.error("Hiba a plot generáláskor:", error);
  }
}
</script>

<style scoped>
.plot-generator {
  max-width: 500px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
}
form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
img {
  max-width: 100%;
  margin-top: 1rem;
  border: 1px solid #ccc;
}
</style>
