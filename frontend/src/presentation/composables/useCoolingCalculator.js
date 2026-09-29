import { ref } from 'vue';
import { CalculateCooling } from '../../application/useCases/CalculateCooling.js';
import { HttpCoolingRepository } from '../../infrastructure/http/HttpCoolingRepository.js';

export function useCoolingCalculator() {
  const result = ref(null);
  const loading = ref(false);
  const error = ref(null);

  const calculateCoolingUseCase = new CalculateCooling(new HttpCoolingRepository());

  const calculate = async (params) => {
    loading.value = true;
    error.value = null;
    try {
      result.value = await calculateCoolingUseCase.execute(params);
    } catch (err) {
      error.value = err.message || 'An unexpected error occurred.';
      result.value = null;
    } finally {
      loading.value = false;
    }
  };

  return {
    result,
    loading,
    error,
    calculate,
  };
}
