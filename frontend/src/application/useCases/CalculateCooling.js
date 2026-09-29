export class CalculateCooling {
  constructor(coolingRepository) {
    this.coolingRepository = coolingRepository;
  }

  async execute(params) {
    if (!params.ambientTemp || !params.initialTemp || !params.momentTemp || !params.momentTime) {
      throw new Error('Missing required calculation parameters');
    }

    if (params.initialTemp === params.ambientTemp) {
      throw new Error('Initial temperature cannot be exactly the ambient temperature.');
    }

    return await this.coolingRepository.calculateCooling(params);
  }
}
