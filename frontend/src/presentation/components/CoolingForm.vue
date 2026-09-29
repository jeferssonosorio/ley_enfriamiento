<script setup>
import { ref } from 'vue';

const emit = defineProps();
const formEmit = defineEmits(['submit']);

const form = ref({
  ambientTemp: 30,
  initialTemp: 80,
  momentTemp: 72,
  momentTime: 3
});

const handleSubmit = () => {
  formEmit('submit', { ...form.value });
};
</script>

<template>
  <form @submit.prevent="handleSubmit" class="cooling-form">
    <div class="form-group">
      <label for="ambientTemp">Temperatura Medio Ambiente (°C)</label>
      <input id="ambientTemp" v-model.number="form.ambientTemp" type="number" step="any" required />
    </div>

    <div class="form-group">
      <label for="initialTemp">Temperatura Inicial (°C)</label>
      <input id="initialTemp" v-model.number="form.initialTemp" type="number" step="any" required />
    </div>

    <div class="form-group">
      <label for="momentTemp">Temperatura en Momento N (°C)</label>
      <input id="momentTemp" v-model.number="form.momentTemp" type="number" step="any" required />
    </div>

    <div class="form-group">
      <label for="momentTime">Tiempo en Momento N (minutos)</label>
      <input id="momentTime" v-model.number="form.momentTime" type="number" step="any" min="0.001" required />
    </div>

    <button type="submit" class="submit-btn">Calcular Enfriamiento</button>
  </form>
</template>

<style scoped>
.cooling-form {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  display: grid;
  gap: 1.5rem;
  grid-template-columns: 1fr 1fr;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

label {
  font-weight: 500;
  color: #475569;
}

input {
  padding: 0.75rem;
  border: 1px solid #cbd5e1;
  border-radius: 4px;
  font-size: 1rem;
}

input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.submit-btn {
  grid-column: 1 / -1;
  background-color: #3b82f6;
  color: white;
  padding: 0.75rem;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s;
}

.submit-btn:hover {
  background-color: #2563eb;
}

@media (max-width: 600px) {
  .cooling-form {
    grid-template-columns: 1fr;
  }
}
</style>
