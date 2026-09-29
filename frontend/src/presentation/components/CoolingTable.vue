<script setup>
defineProps({
  items: {
    type: Array,
    required: true,
  }
});
</script>

<template>
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th>Paso (n)</th>
          <th>Tiempo (t)</th>
          <th>Temperatura T(t)</th>
          <th>ΔT (Inicial - T)</th>
          <th>ΔTm (T - Ambiente)</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.position">
          <td>{{ item.position }}</td>
          <td>{{ item.time }} min</td>
          <td>{{ item.temperature }} °C</td>
          <td>{{ item.tempDifferential }} °C</td>
          <td>{{ item.ambientDifferential }} °C</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.table-container {
  overflow-x: auto;
  margin-top: 1.5rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

table {
  width: 100%;
  border-collapse: collapse;
  background: white;
}

th, td {
  padding: 12px 15px;
  text-align: right;
  border-bottom: 1px solid #e2e8f0;
}

th {
  background-color: #f8fafc;
  font-weight: 600;
  color: #334155;
}

tbody tr:hover {
  background-color: #f1f5f9;
}
</style>
