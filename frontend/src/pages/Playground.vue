<template>
  <section class="playground-page">
    <div v-if="step === 0" class="intro">
      <h1>Seaborn Feature Explorer</h1>
      <p class="intro-text">
        Discover Seaborn's capabilities step by step using the <code>tips</code> dataset. Click start to begin the guided demo.
      </p>
      <button class="start-btn" @click="nextStep">Start</button>
    </div>

    <div v-else-if="step === 1">
      <TipsDatasetInfo />
      <NavigationButtons :onNext="nextStep" />
    </div>

    <div v-else-if="step === 2">
      <StyleShowcase />
      <NavigationButtons :onNext="nextStep" :onPrev="prevStep" />
    </div>

    <div v-else-if="step === 3">
      <BarAggregationDemo />
      <NavigationButtons :onNext="nextStep" :onPrev="prevStep" />
    </div>

    <div v-else-if="step === 4">
      <DistributionDemo />
      <NavigationButtons :onNext="nextStep" :onPrev="prevStep" />
    </div>

    <!-- Additional steps can go here -->
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import TipsDatasetInfo from '@/components/TipsDataSetInfo.vue'
import StyleShowcase from '@/components/StyleShowcase.vue'
import NavigationButtons from '@/components/NavigationButtons.vue'
import BarAggregationDemo from '@/components/BarAggregationDemo.vue'
import DistributionDemo from '@/components/DistributionDemo.vue'

const step = ref(0)
const nextStep = () => step.value++
const prevStep = () => step.value--
</script>

<style scoped>
.playground-page {
  padding: 2rem;
  max-width: 900px;
  margin: 0 auto;
  text-align: center;
}

.intro {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  margin-top: 3rem;
}

.intro h1 {
  font-size: 2.5rem;
  color: #807dbc;
}

.intro-text {
  font-size: 1.2rem;
  max-width: 700px;
  color: #c7e3ea;;
}

.start-btn {
  padding: 0.75rem 2rem;
  background-color: #7DB0BC;
  color: white;
  border: none;
  border-radius: 0.5rem;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.start-btn:hover {
  background-color: #7DB0BC;
}
</style>