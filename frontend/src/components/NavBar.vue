<template>
    <nav class="navbar">
      <div class="nav-container">
        <router-link to="/" class="logo">Seaborn Demo</router-link>
        <button class="hamburger" @click="toggleMenu">☰</button>
        <div class="nav-links" :class="{ open: menuOpen }">
          <router-link to="/playground" class="nav-item" @click="closeMenu">Interaktív</router-link>
          <router-link to="/compare" class="nav-item" @click="closeMenu">Összehasonlítás</router-link>
          <router-link to="/random" class="nav-item" @click="closeMenu">Random</router-link>
        </div>
      </div>
    </nav>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue'
  
  const menuOpen = ref(false)
  
  function toggleMenu() {
    menuOpen.value = !menuOpen.value
  }
  
  function closeMenu() {
    menuOpen.value = false
  }
  </script>
  
  <style scoped>
  .navbar {
    background-color: #1e293b;
    padding: 1rem 2rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    width: 100%;
    z-index: 1000;
  }
  
  .nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: white;
    text-decoration: none;
  }
  
  .hamburger {
    display: none;
    font-size: 1.5rem;
    background: none;
    border: none;
    color: white;
    cursor: pointer;
  }
  
  .nav-links {
    display: flex;
    gap: 1.5rem;
  }
  
  .nav-item {
    color: #cbd5e1;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s;
  }
  
  .nav-item:hover {
    color: white;
  }
  
  .router-link-exact-active {
    color: #3b82f6;
    font-weight: bold;
  }
  
  /* Responsive */
  @media (max-width: 768px) {
    .hamburger {
      display: block;
    }
  
    .nav-links {
      display: none;
      flex-direction: column;
      background-color: #1e293b;
      position: absolute;
      top: 100%;
      right: 0;
      width: 100%;
      padding: 1rem;
    }
  
    .nav-links.open {
      display: flex;
    }
  
    .nav-item {
      padding: 0.5rem 0;
      text-align: center;
    }
  }
  </style>