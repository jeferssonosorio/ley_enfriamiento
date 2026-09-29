<script setup>
import { computed } from 'vue';
import { Line } from 'vue-chartjs';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const props = defineProps({
  items: {
    type: Array,
    required: true,
  },
  ambientTemp: {
    type: Number,
    required: true,
  }
});

const chartData = computed(() => {
  return {
    labels: props.items.map(item => item.time),
    datasets: [
      {
        label: 'Temperatura del Objeto (°C)',
        backgroundColor: '#f87979',
        borderColor: '#f87979',
        data: props.items.map(item => item.temperature),
        tension: 0.4
      },
      {
        label: 'Temperatura Ambiente (°C)',
        backgroundColor: '#82ca9d',
        borderColor: '#82ca9d',
        borderDash: [5, 5],
        data: props.items.map(() => props.ambientTemp),
        fill: false,
      }
    ]
  };
});

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    title: {
      display: true,
      text: 'Desarrollo de Temperatura respecto al Tiempo'
    }
  },
  scales: {
    x: {
      title: {
        display: true,
        text: 'Tiempo (minutos)'
      }
    },
    y: {
      title: {
        display: true,
        text: 'Temperatura (°C)'
      }
    }
  }
};
</script>

<template>
  <div class="chart-container">
    <Line :data="chartData" :options="chartOptions" />
  </div>
</template>

<style scoped>
.chart-container {
  position: relative;
  height: 400px;
  width: 100%;
  background: white;
  padding: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
</style>
