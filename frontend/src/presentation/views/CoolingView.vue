<script setup>
import { ref } from 'vue';
import { useCoolingCalculator } from '../composables/useCoolingCalculator';
import CoolingForm from '../components/CoolingForm.vue';
import CoolingChart from '../components/CoolingChart.vue';
import CoolingTable from '../components/CoolingTable.vue';

const { result, loading, error, calculate } = useCoolingCalculator();
const currentAmbientTemp = ref(30);

const handleCalculate = async (params) => {
  currentAmbientTemp.value = params.ambientTemp;
  await calculate(params);
};
</script>

<template>
  <div class="cooling-view">
    <header>
      <h1>Ley de Enfriamiento de Newton</h1>
      <p>Simulación del decaimiento térmico</p>
    </header>

    <main class="content">
      <section class="configuration-section">
        <CoolingForm @submit="handleCalculate" />
        
        <div v-if="error" class="error-message">
          {{ error }}
        </div>
      </section>

      <div v-if="loading" class="loading-state">
        Calculando iteraciones...
      </div>

      <section v-else-if="result" class="results-section">
        <div class="k-result-card">
          <h3>Constante de Proporcionalidad (K)</h3>
          <div class="k-value">{{ result.constantK }}</div>
        </div>

        <CoolingChart :items="result.items" :ambient-temp="currentAmbientTemp" />
        
        <CoolingTable :items="result.items" />
      </section>
    </main>
  </div>
</template>

<style scoped>
.cooling-view {
  max-width: 1000px;
  margin: 0 auto;
  padding: 2rem;
}

header {
  text-align: center;
  margin-bottom: 2rem;
}

header h1 {
  color: #1e293b;
  margin-bottom: 0.5rem;
}

header p {
  color: #64748b;
  font-size: 1.1rem;
}

.content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.error-message {
  background-color: #fee2e2;
  color: #dc2626;
  padding: 1rem;
  border-radius: 4px;
  margin-top: 1rem;
  border: 1px solid #fecaca;
}

.loading-state {
  text-align: center;
  color: #64748b;
  padding: 3rem;
  font-size: 1.2rem;
}

.results-section {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.k-result-card {
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  padding: 1.5rem;
  border-radius: 8px;
  text-align: center;
}

.k-result-card h3 {
  color: #166534;
  margin: 0 0 0.5rem 0;
  font-size: 1.1rem;
}

.k-value {
  font-size: 2.5rem;
  font-weight: bold;
  color: #15803d;
}
</style>
