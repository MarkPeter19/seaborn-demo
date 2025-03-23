<template>
  <section class="landing">
    <h1>Seaborn Demo 🧠📊</h1>
    <p>
      A modern, stílusos adatvizualizációs könyvtár Pythonhoz. Ez az oldal élő
      példákon keresztül mutatja be a Seaborn lehetőségeit.
    </p>
    <div class="buttons">
      <router-link to="/playground" class="btn"
        >Próbáld ki élőben →</router-link
      >
      <router-link to="/compare" class="btn secondary"
        >Seaborn vs Matplotlib →</router-link
      >
      <router-link to="/random" class="btn warning"
        >Random Charts →</router-link
      >
    </div>
  </section>

  <section class="info">
    <h2>Miért jobb a Seaborn?</h2>
    <ul>
      <li>
        <strong>Szebb alapértelmezett stílus:</strong> Seaborn automatikusan
        formázza a színeket, hátteret, tengelyeket
      </li>
      <li>
        <strong>Könnyebb magas szintű grafikonok:</strong> kevesebb kód, több
        stílus
      </li>
      <li>
        <strong>Témák és paletták egyszerű kezelése:</strong> például
        <code>set_theme()</code>, <code>palette="pastel"</code>
      </li>
    </ul>
    <p>
      Az alábbi példák élő összehasonlítással mutatják meg a különbséget
      ugyanazon adatokkal.
    </p>
  </section>
</template>

<script setup lang="ts"></script>

<style scoped>
.landing {
  text-align: center;
  padding: 4rem 2rem 2rem;
}

h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

p {
  font-size: 1.25rem;
  max-width: 700px;
  margin: 0 auto 2rem;
}

.buttons {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 2rem;
}

.btn {
  padding: 0.75rem 1.5rem;
  background-color: #3b82f6;
  color: white;
  border-radius: 0.5rem;
  text-decoration: none;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #2563eb;
}

.btn.secondary {
  background-color: #10b981;
}

.btn.secondary:hover {
  background-color: #059669;
}

.btn.warning {
  background-color: #f59e0b;
}
.btn.warning:hover {
  background-color: #d97706;
}

.info {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  font-size: 1rem;
  line-height: 1.6;
}

.info h2 {
  font-size: 1.75rem;
  margin-bottom: 1rem;
  text-align: center;
}

.info ul {
  text-align: left;
  padding-left: 1.5rem;
  margin-bottom: 1.5rem;
}

.info li {
  margin-bottom: 0.75rem;
}
</style>
