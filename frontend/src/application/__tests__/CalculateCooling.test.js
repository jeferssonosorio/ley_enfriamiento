import { describe, it, expect, vi } from 'vitest';
import { CalculateCooling } from '../useCases/CalculateCooling.js';
import { CoolingApiRepository } from '../ports/CoolingRepository.js';

describe('Application - CalculateCooling UseCase', () => {
  it('should validate missing parameters', async () => {
    const mockRepo = new CoolingApiRepository();
    const useCase = new CalculateCooling(mockRepo);

    await expect(useCase.execute({
      ambientTemp: 30,
      initialTemp: 80
      // Missing momentTemp and momentTime
    })).rejects.toThrow('Missing required calculation parameters');
  });

  it('should validate if initialTemp equals ambientTemp', async () => {
    const mockRepo = new CoolingApiRepository();
    const useCase = new CalculateCooling(mockRepo);

    await expect(useCase.execute({
      ambientTemp: 30,
      initialTemp: 30,
      momentTemp: 25,
      momentTime: 3
    })).rejects.toThrow('Initial temperature cannot be exactly the ambient temperature.');
  });

  it('should execute successfully when parameters are valid', async () => {
    class MockRepo extends CoolingApiRepository {
      async calculateCooling() {
        return { constantK: -0.1, items: [] };
      }
    }
    
    const mockRepo = new MockRepo();
    const spy = vi.spyOn(mockRepo, 'calculateCooling');
    const useCase = new CalculateCooling(mockRepo);

    const validParams = {
      ambientTemp: 50,
      initialTemp: 80,
      momentTemp: 72,
      momentTime: 3
    };

    const result = await useCase.execute(validParams);
    
    expect(spy).toHaveBeenCalledWith(validParams);
    expect(result.constantK).toBe(-0.1);
  });
});
