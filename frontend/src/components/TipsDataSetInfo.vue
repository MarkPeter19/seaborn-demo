<template>
    <section class="dataset-info">
      <p><strong>Használt adathalmaz:</strong> <code>tips</code></p>
      <p>Ez egy éttermi adathalmaz, ahol a vendégek számláinak összegét, borravalóját és néhány jellemzőjüket rögzítették.</p>
      <table class="data-table">
        <thead>
          <tr>
            <th>total_bill</th>
            <th>tip</th>
            <th>sex</th>
            <th>smoker</th>
            <th>day</th>
            <th>time</th>
            <th>size</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>16.99</td>
            <td>1.01</td>
            <td>Female</td>
            <td>No</td>
            <td>Sun</td>
            <td>Dinner</td>
            <td>2</td>
          </tr>
          <tr>
            <td>21.01</td>
            <td>3.00</td>
            <td>Male</td>
            <td>No</td>
            <td>Sun</td>
            <td>Dinner</td>
            <td>3</td>
          </tr>
          <tr>
            <td>23.68</td>
            <td>3.31</td>
            <td>Male</td>
            <td>No</td>
            <td>Sun</td>
            <td>Dinner</td>
            <td>2</td>
          </tr>
        </tbody>
      </table>
    </section>
  </template>
  
  <script setup lang="ts">
  </script>
  
  <style scoped>
  .dataset-info {
    background-color: #1e1e1e;
    border: 1px solid #3f506a;
    padding: 1rem;
    border-radius: 0.75rem;
    margin-bottom: 2rem;
    text-align: left;
  }
  
  .data-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
    font-size: 0.9rem;
  }
  
  .data-table th,
  .data-table td {
    border: 1px solid #3f506a;
    padding: 0.5rem 0.75rem;
    text-align: center;
  }
  
  .data-table thead {
    background-color:#374151;
  }
  </style>