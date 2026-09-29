import { describe, it, expect, vi } from 'vitest';
import { useCoolingCalculator } from '../composables/useCoolingCalculator.js';
import * as CalculateCoolingModule from '../../application/useCases/CalculateCooling.js';

// Setup Mock for dependencies
vi.mock('../../application/useCases/CalculateCooling.js');
vi.mock('../../infrastructure/http/HttpCoolingRepository.js');

describe('Presentation - useCoolingCalculator', () => {
  it('should initialize with default states', () => {
    const { result, loading, error } = useCoolingCalculator();

    expect(result.value).toBeNull();
    expect(loading.value).toBe(false);
    expect(error.value).toBeNull();
  });

  it('should set loading to true and false during execution', async () => {
    const executeMock = vi.fn().mockResolvedValue({
      constantK: -0.1,
      items: []
    });

    CalculateCoolingModule.CalculateCooling.mockImplementation(() => ({
      execute: executeMock
    }));

    const { loading, result, calculate } = useCoolingCalculator();

    const calculatePromise = calculate({
      ambientTemp: 30,
      initialTemp: 80,
      momentTemp: 70,
      momentTime: 3
    });

    expect(loading.value).toBe(true);

    await calculatePromise;

    expect(loading.value).toBe(false);
    expect(result.value.constantK).toBe(-0.1);
  });

  it('should catch errors and update the error state', async () => {
    const executeMock = vi.fn().mockRejectedValue(new Error('API failed'));

    CalculateCoolingModule.CalculateCooling.mockImplementation(() => ({
      execute: executeMock
    }));

    const { error, result, calculate } = useCoolingCalculator();
    
    await calculate({ ambientTemp: 30, initialTemp: 30 }); 
    
    expect(result.value).toBeNull();
    expect(error.value).toBe('API failed');
  });
});
